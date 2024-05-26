import re
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
from phtml import StyleTag
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

        if remaining_content.startswith('<!DOCTYPE html>'):
            remaining_content = remaining_content[15:].strip()
            is_document = True
        else:
            is_document = False

        loop_active = True
        while loop_active:
            element, remaining_content = self.find_next_element(
                remaining_content=remaining_content.strip(),
                current_element=current_element
            )
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

    def find_next_element(self, remaining_content, current_content='', current_element=None):
        match_str = re.search(r'<(([a-z0-9-]+) ?|!--)', remaining_content)
        if match_str:
            if match_str.start() > 0:
                element = remaining_content[:match_str.start()]
                remaining_content = remaining_content[match_str.start():]
                return element, remaining_content
            if match_str.groups(0)[1] == 0:
                tag_str = match_str.groups(0)[0]
            else:
                tag_str = match_str.groups(0)[1]
            """
            At this point we are assuming remaining_content starts with a tag
            But it does not need to end with that same tag, there could be more
            """
            mapping = self.tag_mapping.from_tag(tag_str)
            tag_start_string = f"<{mapping['tag_start']}"
            if mapping['tag_end'] is None:
                tag_end_string = f">"
            else:
                if mapping['class'] == 'Comment':
                    tag_end_string = f"-->"
                else:
                    tag_end_string = f"</{mapping['tag_end']}>"
            depth = 1
            tag_info_grabbed = False
            for i in range(1, len(remaining_content)):
                if remaining_content[i] == '>' and not tag_info_grabbed:
                    tag_info = remaining_content[len(tag_start_string):i].strip()
                    content_start_index = i+1
                    tag_info_grabbed = True
                elif remaining_content[i:i+2] == '--' and not tag_info_grabbed:
                    # Found the end of the start of as comment tag
                    tag_info = ''
                    content_start_index = i+2
                    tag_info_grabbed = True
                if remaining_content[i:i+len(tag_start_string)] == tag_start_string:
                    # Found nested same tag type
                    depth += 1
                if remaining_content[i:i+len(tag_end_string)] == tag_end_string:
                    # Found end of tag or nested tag
                    depth -= 1
                if depth == 0:
                    # We have the full tag
                    content_end_index = i
                    tag_content = remaining_content[content_start_index:content_end_index]
                    remaining_content = remaining_content[i+len(tag_end_string):]
                    tag_info = tag_info.strip()
                    tag_content = tag_content.strip()
                    remaining_content = remaining_content.strip()
                    break
            if 'class=' in tag_info:
                print(tag_info)
                class_re_match = re.search(r'class="([^"]+)"', tag_info)
                if class_re_match:
                    class_info = class_re_match.groups()[0]
                else:
                    class_info = ''
            else:
                class_info = None
            if 'style=' in tag_info:
                print(tag_info)
                style_re_match = re.search(r'style="([^"]+)"', tag_info)
                if style_re_match:
                    style_info = style_re_match.groups()[0]
                else:
                    style_info = ''
            else:
                style_info = None
            tag_dict = {}
            if tag_content:
                internal = []
                running = True
                while running:
                    element, tag_content = self.find_next_element(remaining_content=tag_content.strip())
                    internal.append(element)
                    if not tag_content.strip():
                        running = False
                tag_dict['internal'] = internal
            if mapping['class'] == 'Header':
                # Header tags are a bit special
                tag_dict['level'] = int(mapping['tag_start'][-1])
            element = globals()[mapping['class']](**tag_dict)
            if class_info:
                element.add_class(class_info)
            if style_info:
                element.add_style(style_info)
            return element, remaining_content
        else:
            # Its a string or non tag element
            return remaining_content, ''

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
