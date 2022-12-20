import re
# from phtml import Document
from phtml.document import Document
from phtml import Base
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
        content = content.replace('\n', '')
        if content.startswith('<!DOCTYPE html>'):
            content = content[15:]
        loop_active = True
        while loop_active:
            loop_active, content, element = self.find_next_element(content, current_element)
            if element is not None:
                contents.append(element)
            x=1
        x=1
        return contents
        pass

    def find_next_element(self, content, current_element=None):
        if content.endswith('<br'):
            x=1
        match_start = re.search(r'<([a-z0-9]+) ?', content)
        element = None
        try:
            int(content)
            x=1
        except:
            pass
        # if content == '5':
        #     x=1
        if match_start:
            if content == '<a>':
                x=1
            if match_start.start() > 0:
                x=1
                element = content[0:match_start.start()]
                content = content[match_start.start():]
                if content.endswith('<br'):
                    x=1
                return True, content, element
            tag_start = match_start.groups(0)[0]
            if tag_start == 'a':
                x=1
            if tag_start == 'br':
                match_start_index = match_start.start()
                match_end_index = match_start.end()
                element = LineBreak()
            elif tag_start == 'link':
                # match_end = re.search(f'/>?$', content)
                match_end = re.search(f'/>$', content)
                match_start_index = match_start.start()
                if match_end is None:
                    x=1
                match_end_index = match_end.end()
            else:
                match_end = re.search(f'</{tag_start}', content)
                match_start_index = match_start.start()
                match_end_index = match_end.end()

            element_string = content[match_start_index:match_end_index]
            if element is None:
                element = self.parse_element(element_string,  tag_start, current_element)
            start_index = max(match_start_index - 1, 0)
            end_index = min(match_end_index + 1, len(content) - 1)
            if content.endswith('<br'):
                x=1
            llll = len(content)
            og_c = content
            if tag_start == 'link':
                content = content[0:start_index] + content[end_index:-1]
            else:
                content = content[0:start_index] + content[end_index:]
            if content.endswith('<br'):
                x=1
        else:
            if content.endswith('<br'):
                x=1
            return False, None, content
        if content.endswith('<br'):
            x=1
        return True, content, element

    def parse_element(self, content, tag, current_element=None):
        tags_string_start = ''
        tags_string_end = ''
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
                    x=1
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
            tags_styles = {}
            for ta in tag_attributes:
                kv = ta.split('=')
                if len(kv) != 2:
                    continue
                key = kv[0]
                value = kv[-1][1:-1]
                if key == 'style':
                    for vi in value.split(';'):
                        if not vi:
                            continue
                        style_key, style_value =  vi.split(':')
                        tags_styles[style_key.strip()] = style_value.strip()
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
        # elif tag == 'br':
        #     found = True
        #     element = LineBreak(**tags_dict)
        elif tag == 'title':
            found = True
            element = Title(**tags_dict)
        if not found and tag not in ['head', 'body']:
            x=1
        if tags_classes:
            [element.add_class(cl) for cl in tags_classes]
        if tags_styles:
            for key, value in tags_styles.items():
                element.add_style({key: value})
        contents = self.read_data(content, current_element)
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
        x=1
        return element


h = HtmlReader()

h.read_file('tests/resources/old_class_builds_for_manipulation.html')

