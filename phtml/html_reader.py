import re
from phtml import Button
from phtml import Document
from phtml import Blockquote
from phtml import Div
from phtml import Header
from phtml import (
    HtmlList,
    HtmlListItem,
)
from phtml import Image
from phtml import Link
from phtml import HyperLink
from phtml import Paragraph
from phtml import Title
from phtml import (
    TextFormat,
    LineBreak,
    Bold,
    Strong,
    Italic,
    Emphasized,
    Marked,
    Smaller,
    Deleted,
    Inserted,
    Subscript,
    Superscript,
    Emoji,
)
from phtml import Style


class HtmlReader:
    def __init__(self):
        pass

    def read_file(self, filepath):
        with open(filepath, 'r') as hf:
            content = hf.read()
        contents = self.read_data(content)
        return contents

    def read_data(self, content, current_element=None):
        contents = []
        remaining_content = content.replace('\n', '')
        main_loop = False
        if remaining_content.startswith('<!DOCTYPE html>'):
            remaining_content = remaining_content[15:].strip()
            main_loop = True
        loop_active = True
        while loop_active:
            # old_content = remaining_content
            loop_active, remaining_content, element = self.find_next_element(
                remaining_content=remaining_content,
                current_element=current_element
            )
            # if main_loop:
            #     x=1
            # x=1
            if element is not None:
                contents.append(element)
        #     x=1
        # x=1
        # if main_loop:
        #     x=1
        return contents

    def find_next_element(self, remaining_content, current_content='', current_element=None):
        match_start = re.search(r'<([a-z0-9]+) ?', remaining_content)
        element = None
        if match_start:
            if match_start.start() > 0:
                element = remaining_content[0:match_start.start()]
                remaining_content = remaining_content[match_start.start():]
                return True, remaining_content, element
            tag_start = match_start.groups(0)[0]
            """
            Some tags need some massaging to be processed or just ignored
            """
            if tag_start == 'br':
                match_start_index = match_start.start()
                match_end_index = match_start.end() + 1
                element = LineBreak()
            elif tag_start == 'link':
                match_end = re.search(f'/?>', remaining_content)
                match_start_index = match_start.start()
                match_end_index = match_end.end()
            else:
                view_window_starts = len(tag_start) + 2
                view_window_ends = len(tag_start) + 2
                loop = True
                while loop:
                    loop = False
                    match_beg = re.search(f'<{tag_start}', remaining_content[view_window_starts:])
                    match_end = re.search(f'</{tag_start}>', remaining_content[view_window_ends:])
                    if match_beg is None:
                        break
                    if (match_beg.start() + view_window_starts) < (match_end.start() + view_window_ends):
                        view_window_starts = view_window_starts + match_beg.end()
                        view_window_ends = view_window_ends + match_end.end()
                        loop = True
                match_start_index = match_start.start()
                try:
                    match_end_index = match_end.end() + view_window_ends
                except Exception as e:
                    e

            """
            Process the tag
            """
            current_content = remaining_content[match_start_index:match_end_index]
            element_string = current_content
            if element is None:
                element = self.parse_element(element_string,  tag_start, current_element)
            start_index = max(match_start_index, 0)
            end_index = min(match_end_index, len(current_content))

            """
            Some tags need a bit more massaging after
            """
            remaining_content = remaining_content[0:start_index] + remaining_content[end_index:]
        else:
            return False, None, remaining_content
        return True, remaining_content, element

    def parse_element(self, content, tag, current_element=None):
        tags_string_start = ''
        tags_string_end = ''
        content = re.sub(r'/ *>$', '>', content, count=1)
        for c in content:
            tags_string_start += c
            if c == '>':
                break
        content = content[len(tags_string_start):]
        for c in reversed(content):
            tags_string_end = c + tags_string_end
            if c == '<':
                break
        content = content[:-len(tags_string_end)]

        if tags_string_start != f"<{tag}>":
            tag_attributes = tags_string_start[:-1].split(' ')[1:]
            modding = True
            while modding:
                modding = False
                new_tag_attributes = []
                for index in range(len(tag_attributes)):
                    item = tag_attributes[index]
                    if not item:
                        del tag_attributes[index]
                        modding = True
                        break
                    if not item.endswith(('"', "'")):
                        try:
                            item += ' ' + tag_attributes[index + 1]
                        except IndexError:
                            pass
                        new_tag_attributes.append(item)
                        new_tag_attributes.extend(tag_attributes[index + 2:])
                        tag_attributes = new_tag_attributes
                        modding = True
                        break
                    new_tag_attributes.append(item)
            tags_dict = {}
            tags_classes = []
            tags_styles = []
            for ta in tag_attributes:
                kv = ta.split('=')
                if len(kv) != 2:
                    continue
                key = kv[0]
                value = kv[-1][1:-1]
                if key == 'style':
                    x=1
                    stl = self.parse_style(style_string=value)
                    x=1
                    tags_styles.extend(stl)
                    # for vi in value.split(';'):
                    #     if not vi:
                    #         continue
                    #     style_key, style_value =  vi.split(':')
                    #     tags_styles[style_key.strip()] = style_value.strip()
                elif key == 'class':
                    for cl in value.split(' '):
                        if cl:
                            tags_classes.append(cl.strip())
                else:
                    tags_dict[key.strip()] = value.strip()
        else:
            tags_dict = {}
            tags_classes = None
            tags_styles = None

        found = False
        if tag == 'html':
            found = True
            element = Document(**tags_dict)
            current_element = element
        elif tag == 'div':
            found = True
            element = Div(**tags_dict)
        elif tag == 'p':
            found = True
            element = Paragraph(**tags_dict)
        elif tag.startswith('h') and len(tag) == 2:
            found = True
            element = Header(level=tag[-1], **tags_dict)
        elif tag == 'a':
            found = True
            element = Link(**tags_dict)
        elif tag == 'link':
            found = True
            element = HyperLink(**tags_dict)
        elif tag == 'title':
            found = True
            element = Title(**tags_dict)
        elif tag == 'button':
            found = True
            element = Button(**tags_dict)
        elif tag == 'style':
            found = True
            element = content
            styles = self.parse_style(content)
            current_element.styles.extend(styles)
            return None
        # if not found and tag not in ['head', 'body']:
        #     x=1
        # if not found and tag not in ['style']:
        #     return ''
        if tags_classes:
            [element.add_class(cl) for cl in tags_classes]
        if tags_styles:
            for style in tags_styles:
                element.add_style(style)
            # for key, value in tags_styles.items():
            #     element.add_style({key: value})
        if content:
            contents = self.read_data(content, current_element)
        else:
            contents = []
        for content in contents:
            try:
                if tag in ['head', 'body'] and isinstance(current_element, Document):
                    getattr(current_element, tag).append(content)
                    element = None
                elif isinstance(element, LineBreak):
                    pass
                else:
                    element.internal.append(content)
            except Exception as e:
                e
                element = None
        if tag == 'html':
            return current_element
        return element

    def parse_style(self, style_string):
        style_string = re.sub(r'\/\*[a-zA-Z0-9.,{}()\[\] :;#\%-]+\*/', '', style_string) # Removing comments
        results = style_string.split('}')
        styles = []
        x=1
        for item in results:
            if item == '':
                continue
            kv = item.split('{')
            if len(kv) == 1:
                name = None
            else:
                name = kv[0].strip()
            style = {}
            for kv in kv[-1].split(';'):
                if kv == '':
                    continue
                key, value = kv.split(':')
                style[key] = value
            styles.append(Style(name=name, style_details=style))
        return styles
