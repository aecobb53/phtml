from code import interact
from hashlib import new
import re
import yaml
from phtml import Base
from phtml import Body
from phtml import Document
from phtml import Style
from phtml import Base
from phtml import Blockquote
from phtml import Inlinequote
from phtml import Button
from phtml import Canvas
from phtml import Comment
from phtml import Div
from phtml import Form
from phtml import Head
from phtml import Html
from phtml import Textarea
from phtml import Select
from phtml import Option
from phtml import Optiongroup
from phtml import Fieldset
from phtml import Label
from phtml import Output
from phtml import Header
from phtml import HtmlList
from phtml import HtmlListItem
from phtml import HyperLink
from phtml import IFrame
from phtml import Image
from phtml import Input
from phtml import Link
from phtml import Meta
from phtml import Noscript
from phtml import Paragraph
from phtml import Script
from phtml import Span
from phtml import Svg
from phtml import TextFormat
from phtml import Table
from phtml import TableRow
from phtml import TableHeader
from phtml import TableData
from phtml import LineBreak
from phtml import Bold
from phtml import Strong
from phtml import Italic
from phtml import Emphasized
from phtml import Marked
from phtml import Smaller
from phtml import Deleted
from phtml import Inserted
from phtml import Subscript
from phtml import Superscript
from phtml import Title
from phtml.classes import style

from .tag_mapping import TagMapping


class HtmlReader:
    def __init__(self):
        self.tag_mapping = TagMapping()

    def read_file(self, filepath):
        with open(filepath, 'r') as hf:
            content = hf.read()
        contents = self.read_data(content)
        return contents

    def read_data(self, content, current_element=None):
        contents = []
        remaining_content = content.replace(r'\s*\n\s*', '')
        # if remaining_content.startswith('<!--'):
        #     x=1
        # main_loop = False

        if remaining_content.startswith('<!DOCTYPE html>'):
            remaining_content = remaining_content[15:].strip()
            is_document = True
        else:
            is_document = False
            # main_loop = True

        # # Remove scripts
        # scripts = []
        # while '</script>' in remaining_content:
        #     script_start = re.search(r'<script', remaining_content).start()
        #     script_end = re.search(r'<\/script>', remaining_content).end()
        #     script = remaining_content[script_start:script_end]
        #     scripts.append(script)
        #     remaining_content = remaining_content[:script_start] + remaining_content[script_end:]

        loop_active = True
        # print(f"Read data: [{remaining_content}]")
        # print(f"Current element: {current_element}")
        while loop_active:
            # print('-----------------------------------')
            # print(f"IN ACTIVE LOOP ========================")
            # print(f"Read data: [{remaining_content}]")
            # print(f"Current element: {current_element}")
            element, remaining_content = self.find_next_element_v2(
                remaining_content=remaining_content.strip(),
                current_element=current_element
            )
            # loop_active, remaining_content, element = self.find_next_element(
            #     remaining_content=remaining_content,
            #     current_element=current_element
            # )
            if element is not None:
                contents.append(element)
            if remaining_content.strip() == '':
                loop_active = False
        if is_document:
            # Assuming the contents is a list of a single element that is a html tag
            kwargs = {}
            for i in contents[0].internal:
                if isinstance(i, Head):
                    kwargs['head'] = i.internal
                elif isinstance(i, Body):
                    kwargs['body'] = i.internal
                elif isinstance(i, Style):
                    kwargs['styles'] = i
                elif isinstance(i, Script):
                    kwargs['scripts'] = i
            contents = [Document(**kwargs)]
        return contents

    def find_next_element_v2(self, remaining_content, current_content='', current_element=None):
        # print('-----------------------------------')
        match_str = re.search(r'<(([a-z0-9-]+) ?|!--)', remaining_content)
        # print(match_str)
        if match_str:
            # print(f"Match str start: {match_str.start()}")
            if match_str.start() > 0:
                # print('Match str > 0')
                element = remaining_content[:match_str.start()]
                remaining_content = remaining_content[match_str.start():]
                # print(f"String element: [{element}]")
                # print(f"String Remaining content: [{remaining_content}]")
                return element, remaining_content
                # return remaining_content, None
                # return True, remaining_content, element
            if match_str.groups(0)[1] == 0:
                tag_str = match_str.groups(0)[0]
            else:
                tag_str = match_str.groups(0)[1]
            """
            At this point we are assuming remaining_content starts with a tag
            But it does not need to end with that same tag, there could be more
            """
            # Need to set it up to parse for the next element, if the element is a string parse until next tag
            # Return only the string or element. Then let things iterate to infinity grabbing stuff as it goes
            # Then bring it all together into a list at the loop stage
            # print(f"Tag str: [{tag_str}]")
            # print(f"remaining_content: [{remaining_content}]")
            # print(f"current_content: [{current_content}]")
            # print(f"RE Match: [{match_str}], [{match_str.groups()}]")
            # if tag_str not in ['html', 'body', 'head']:
            # if tag_str in ['html', 'body', 'head']:
            #     # Its a tag were not dealing with 
            #     return 
            # else:
            mapping = self.tag_mapping.from_tag(tag_str)
            # print(f"Mapping: [{mapping}]")
            tag_start_string = f"<{mapping['tag_start']}"
            if mapping['tag_end'] is None:
                tag_end_string = f">"
            else:
                if mapping['class'] == 'Comment':
                    tag_end_string = f"-->"
                else:
                    tag_end_string = f"</{mapping['tag_end']}>"
            depth = 1
            # print(f"tag_start_string: {tag_start_string}")
            # print(f"tag_end_string: {tag_end_string}")
            # print(f"depth: {depth}")
            tag_info_grabbed = False
            for i in range(1, len(remaining_content)):
                # print(f"i: {i}, {remaining_content[i]}")
                # print(remaining_content[i:i+len(tag_start_string)])
                # print(remaining_content[i:i+len(tag_end_string)])
                if remaining_content[i] == '>' and not tag_info_grabbed:
                    # Found the end of the start of the tag
                    # print('')
                    # print('ONE')
                    tag_info = remaining_content[len(tag_start_string):i].strip()
                    # tag_content = remaining_content[i+1:]
                    # print(f"Tag info: [{tag_info}]")
                    # print(f"Tag content: [{tag_content}]")
                    # print('')
                    content_start_index = i+1
                    tag_info_grabbed = True
                elif remaining_content[i:i+2] == '--' and not tag_info_grabbed:
                    # Found the end of the start of as comment tag
                    tag_info = ''
                    content_start_index = i+2
                    tag_info_grabbed = True
                if remaining_content[i:i+len(tag_start_string)] == tag_start_string:
                    # Found nested same tag type
                    # print('TWO')
                    depth += 1
                if remaining_content[i:i+len(tag_end_string)] == tag_end_string:
                    # Found end of tag or nested tag
                    # print('THREE')
                    depth -= 1
                if depth == 0:
                    # We have the full tag
                    content_end_index = i
                    # print('')
                    # print('FOUR')
                    # print(f"i: [{i}], len(tag_end_string): [{len(tag_end_string)}]")
                    full_tag = remaining_content[:i+len(tag_end_string)]
                    # print(len(tag_end_string))
                    # print(len(tag_end_string)+1)
                    # print(-(len(tag_end_string)+1))
                    # print(f"tag_info: [{tag_info}]")
                    # print(f"Remain content focus: [{remaining_content[i+len(tag_info):i]}]")
                    # print(f"Remain content focus: [{remaining_content[len(tag_start_string)+len(tag_info)+1:i]}]")
                    # tag_content = tag_content[:-(len(tag_end_string)+1)]
                    # tag_content = remaining_content[i+len(tag_info):i]
                    # print(f"tag_start_string: [{tag_start_string}]")
                    # print(f"tag_info: [{tag_info}]")
                    # tag_content = remaining_content[len(tag_start_string)+len(tag_info)+1:i]
                    tag_content = remaining_content[content_start_index:content_end_index]
                    remaining_content = remaining_content[i+len(tag_end_string):]
                    tag_info = tag_info.strip()
                    tag_content = tag_content.strip()
                    remaining_content = remaining_content.strip()
                    # print(f"full_tag: [{full_tag}]")
                    # print(f"tag_content: [{tag_content}]")
                    # print(f"remaining_content: [{remaining_content}]")
                    # print('')
                    break
            # tag_content = remaining_content[len(tag_start_string):i]
            if 'class' in tag_info:
                class_re_match = re.search(r'class="([^"]+)"', tag_info)
                # print(f"class_re_match: {class_re_match}")
                # print(f"class_re_match: {class_re_match.groups()[0]}")
                class_info = class_re_match.groups()[0]
            else:
                class_info = None
            if 'style' in tag_info:
                style_re_match = re.search(r'style="([^"]+)"', tag_info)
                style_info = style_re_match.groups()[0]
            else:
                style_info = None
            # print(f"tag_info: \n{tag_info}")
            # print(f"class_info: \n{class_info}")
            # print(f"style_info: \n{style_info}")
            # print(f"tag_content: \n{tag_content}")
            # print(f"full_tag: \n{full_tag}")
            # print(f"new remaining_content: \n{remaining_content}")
            tag_dict = {}
            if tag_content:
                # print('IN TAG CONTENT')
                internal = []
                running = True
                while running:
                    # next_element = self.find_next_element_v2(remaining_content=tag_content.strip())
                    element, tag_content = self.find_next_element_v2(remaining_content=tag_content.strip())
                    # print(f"next_element: [{element}]")
                    # print(f"next_tag_content: [{tag_content}]")
                    internal.append(element)
                    if not tag_content.strip():
                        running = False
                tag_dict['internal'] = internal
            if mapping['class'] == 'Header':
                # Header tags are a bit special
                tag_dict['level'] = int(mapping['tag_start'][-1])
            # print(f"tag_dict: \n{tag_dict}")
            element = globals()[mapping['class']](**tag_dict)
            if class_info:
                element.add_class(class_info)
            if style_info:
                element.add_style(style_info)
            # print(f"element: {element}")
            # if isinstance(element, TextFormat):
            #     print(f"element content: [{element}]")
            # else:
            #     print(f"element content: [{element.return_string_version}]")
            # print(f"final from find remaining_content: [{remaining_content}]")
            return element, remaining_content
        else:
            # Its a string or non tag element
            return remaining_content, ''
                # return True, remaining_content, obj
                # obj = self.parse_element(element_string,  tag_start, current_element)
                    # if tag_start_string in remaining_content[i:]:
                    #     depth += 1
                    # if tag_end_string in remaining_content[i:]:
                    #     depth -= 1
                    # if depth == 0:
                    #     break
        #         # match_start
        #         # A_internal_content = remaining_content[(1 + len(mapping['tag_start'])):]
        #         # if mapping['tag_end'] is not None:
        #         #     match_end = re.search(f'</{mapping["tag_end"]}>', A_internal_content)
        #         #     if match_end is not None:
        #         #         internal_content = A_internal_content[:match_end.end()]
        #         #         remaining_content = A_internal_content[match_end.end():]
        #         #     else:
        #         #         internal_content = A_internal_content
        #         #         remaining_content = ''
        #     if tag_start == 'br':
        #         match_start_index = match_start.start()
        #         match_end_index = match_start.end() + 1
        #         element = LineBreak()
        #     elif tag_start == 'link':
        #         match_end = re.search(f'/?>', remaining_content)
        #         match_start_index = match_start.start()
        #         match_end_index = match_end.end()
        #     else:
        #         view_window_starts = len(tag_start) + 2
        #         view_window_ends = len(tag_start) + 2
        #         loop = True
        #         # if remaining_content.startswith('<meta property="og:description"'):
        #         #     x=1
        #         while loop:
        #             loop = False
        #             match_beg = re.search(f'<{tag_start}', remaining_content[view_window_starts:])
        #             match_end = re.search(f'</{tag_start}>', remaining_content[view_window_ends:])
        #             if match_end is None:
        #                 match_end = re.search(f'>', remaining_content[view_window_ends:])
        #             if match_beg is None:
        #                 break
        #             try:
        #                 if (match_beg.start() + view_window_starts) < (match_end.start() + view_window_ends):
        #                     view_window_starts = view_window_starts + match_beg.end()
        #                     view_window_ends = view_window_ends + match_end.end()
        #                     loop = True
        #             except AttributeError as e:
        #                 x=1
        #         match_start_index = match_start.start()
        #         try:
        #             match_end_index = match_end.end() + view_window_ends
        #         except Exception as e:
        #             e

        #     """
        #     Process the tag
        #     """
        #     try:
        #         current_content = remaining_content[match_start_index:match_end_index]
        #     except Exception as e:
        #         match_end_index = len(remaining_content)
        #         current_content = remaining_content[match_start_index:match_end_index]
        #         e
        #     element_string = current_content
        #     if element is None:
        #         element = self.parse_element(element_string,  tag_start, current_element)
        #     start_index = max(match_start_index, 0)
        #     end_index = min(match_end_index, len(current_content))

        #     """
        #     Some tags need a bit more massaging after
        #     """
        #     remaining_content = remaining_content[0:start_index] + remaining_content[end_index:]
        # else:
        #     return False, None, remaining_content
        # return True, remaining_content, element

    def find_next_element(self, remaining_content, current_content='', current_element=None):
        # if remaining_content.startswith('<!'):
        #     x=1
        # match_start = re.search(r'<([a-z0-9-]+) ?', remaining_content)
        # if remaining_content.startswith('<br'):
        #     print('FOUND Break')
        # if remaining_content.startswith('<meta'):
        #     print('FOUND META')
        # if 'meta' in remaining_content:
        #     print('FOUND META somewhere')
        match_start = re.search(r'<(([a-z0-9-]+) ?|!--)', remaining_content)
        # print(f"match_start: {match_start}")
        element = None
        if match_start:
            # a = match_start.groups(0)
            # b = match_start.groups(1)
            if match_start.start() > 0:
                element = remaining_content[0:match_start.start()]
                remaining_content = remaining_content[match_start.start():]
                return True, remaining_content, element
            if match_start.groups(0)[1] == 0:
                tag_start = match_start.groups(0)[0]
            else:
                tag_start = match_start.groups(0)[1]
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
                # if remaining_content.startswith('<meta property="og:description"'):
                #     x=1
                while loop:
                    loop = False
                    match_beg = re.search(f'<{tag_start}', remaining_content[view_window_starts:])
                    match_end = re.search(f'</{tag_start}>', remaining_content[view_window_ends:])
                    if match_end is None:
                        match_end = re.search(f'>', remaining_content[view_window_ends:])
                    if match_beg is None:
                        break
                    try:
                        if (match_beg.start() + view_window_starts) < (match_end.start() + view_window_ends):
                            view_window_starts = view_window_starts + match_beg.end()
                            view_window_ends = view_window_ends + match_end.end()
                            loop = True
                    except AttributeError as e:
                        x=1
                match_start_index = match_start.start()
                try:
                    match_end_index = match_end.end() + view_window_ends
                except Exception as e:
                    e

            """
            Process the tag
            """
            try:
                current_content = remaining_content[match_start_index:match_end_index]
            except Exception as e:
                match_end_index = len(remaining_content)
                current_content = remaining_content[match_start_index:match_end_index]
                e
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
        print('')
        print(f"Tag: [{tag}]")
        if tag == 'html':
            element = Document(**tags_dict)
            current_element = element
            found = True
        elif tag == 'head':
            pass
        elif tag == 'body':
            pass
        else:
            mapping = self.tag_mapping.from_tag(tag)
            # print(tag)
            print(f"Mapping: [{mapping}]")
            if mapping['class'] == 'Header':
                tags_dict['level'] = tag[-1]
            print(f"Tags Dict[{tags_dict}]")
            print(f"Content [{content}]")
            element = globals()[mapping['class']](**tags_dict)
            # print(f"Element: [{element}], [{mapping}]")
            found = True
            # try:
            #     mapping = self.tag_mapping.from_tag(tag)
            #     print(mapping)
            #     if mapping['class'] == 'Header':
            #         tags_dict['level'] = tag[-1]
            #     # print(tags_dict)
            #     element = globals()[mapping['class']](**tags_dict)
            #     # print(f"Element: [{element}], [{mapping}]")
            #     found = True
            # except Exception as e:
            #     print(f"Tag: [{tag}]")
            #     print(f"Tags Dict: [{tags_dict}]")
            #     print(f"Tags Classes: [{tags_classes}]")
            #     print(f"Tags Styles: [{tags_styles}]")
            #     print(f"Content: [{content}]")
            #     print(f"Mapping not found for tag [{tag}]")
            #     print(e)
        # if tag == 'html':
        #     found = True
        #     element = Document(**tags_dict)
        #     current_element = element
        # elif tag == 'div':
        #     found = True
        #     element = Div(**tags_dict)
        # elif tag == 'p':
        #     found = True
        #     element = Paragraph(**tags_dict)
        # elif tag.startswith('h') and len(tag) == 2:
        #     found = True
        #     element = Header(level=tag[-1], **tags_dict)
        # elif tag == 'a':
        #     found = True
        #     element = Link(**tags_dict)
        # elif tag == 'link':
        #     found = True
        #     element = HyperLink(**tags_dict)
        # elif tag == 'img':
        #     found = True
        #     element = Image(**tags_dict)
        # elif tag == 'title':
        #     found = True
        #     element = Title(**tags_dict)
        # elif tag == 'button':
        #     found = True
        #     element = Button(**tags_dict)
        # elif tag == 'span':
        #     found = True
        #     element = Span(**tags_dict)
        # elif tag == 'meta':
        #     found = True
        #     element = Meta(**tags_dict)
        # elif tag == 'input':
        #     found = True
        #     element = Input(**tags_dict)
        # elif tag == 'svg':
        #     found = True
        #     element = Svg(**tags_dict)
        # elif tag == 'canvas':
        #     found = True
        #     element = Canvas(**tags_dict)
        # elif tag == 'iframe':
        #     found = True
        #     element = IFrame(**tags_dict)
        # elif tag == 'noscript':
        #     found = True
        #     element = Noscript(**tags_dict)
        # elif tag == '!--':
        #     found = True
        #     element = Comment(**tags_dict)
        # elif tag == 'style':
        #     found = True
        #     element = content
        #     styles = self.parse_style(content)
        #     current_element.styles.extend(styles)
        #     return None
        # else:
        #     if tag not in ['head', 'body']:
        #         x=1
        #         # raise TypeError(f'I am unsure what {tag} tag is')
        if tags_classes:
            try:
                [element.add_class(cl) for cl in tags_classes]
            except NameError:
                pass
            except Exception as e:
                e
        if tags_styles:
            for style in tags_styles:
                try:
                    element.add_style(style)
                except NameError:
                    pass
            # for key, value in tags_styles.items():
            #     element.add_style({key: value})
        if content:
            try:
                if isinstance(element, (Svg)):
                    contents = self.read_data(content, element)
                else:
                    contents = self.read_data(content, current_element)
            except UnboundLocalError:
                contents = self.read_data(content, current_element)
        else:
            contents = []
        for content in contents:
            try:
                if tag in ['head', 'body'] and isinstance(current_element, Document):
                    # if content.strip() == '':
                    #     x=1
                    #     content = ''
                    # # else:
                    # #     x=1
                    getattr(current_element, tag).append(content)
                    # getattr(current_element, tag).append(content)
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
        try:
            return element
        except Exception as e:
            e
            return None

    def parse_style(self, style_string):
        style_string = re.sub(r'\/\*[a-zA-Z0-9.,{}()\[\] :;#\%-]+\*/', '', style_string) # Removing comments
        results = style_string.split('}')
        styles = []
        for item in results:
            if item == '':
                continue
            kv = item.split('{')
            kv[-1] = kv[-1].strip()
            if len(kv) == 1:
                name = None
            else:
                name = kv[0].strip()
            style = {}
            for nkv in kv[-1].split(';'):
                nkv = nkv.strip()
                if nkv == '':
                    continue
                key, value = nkv.split(':')
                style[key] = value
            styles.append(Style(name=name, style_details=style))
        return styles

    def read_css_file(self, filepath):
        with open(filepath, 'r') as cf:
            data = cf.read()
        data = data.replace('\n', '')
        return self.parse_style(data)
