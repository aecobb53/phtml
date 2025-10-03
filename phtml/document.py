from . import Base
from . import Html
from . import Head
from . import Body
from . import TextFormat
from . import Style
from . import Script
from . import HyperLink
import re


class Document:
    def __init__(self, head: Head = None, body: Body = None, **kwargs):
        self.head = head
        self.body = body

        if not self.head:
            self.head = Head()
        if not self.body:
            self.body = Body()

        self.styles = []
        self.scripts = []
        self.indent = '    '

    def add_head_element(self, obj):
        self.head.add_element(obj)
        return self

    def add_body_element(self, obj):
        self.body.add_element(obj)
        return self

    def set_indent_width(self, width=4):
        self.indent = ' ' * width
        return self

    @property
    def return_document(self):
        details = []
        details.append('<!DOCTYPE html>')
        html_element = Html(internal=[self.head, self.body])
        details.extend(html_element.return_document)
        return '\n'.join(details)

    def add_style(self, style_obj: Style):
        self.head.add_global_style(style_obj)
        return self

    def add_favicon(self, image_path):
        favicon = HyperLink(rel='icon', href=image_path, type='image/x-icon')
        self.add_head_element(favicon)

    def load_css_file(self, file_path):
        with open(file_path, 'r') as cf:
            css_file_content = cf.read()
        css_elements = re.findall(r'([^{]+)\{([^}]+)\}', re.sub(r'/\*.*?\*/', '', css_file_content, flags=re.DOTALL))
        for element in css_elements:
            selector = element[0].strip()
            styles = element[1].strip().split(';')
            style_details = {}
            for style in styles:
                if style.strip() == '':
                    continue
                key, value = style.split(':')
                style_details[key.strip()] = value.strip()
            style_obj = Style(style_details=style_details, name=selector)
            self.add_style(style_obj)
        return self

    def load_js_file(self, file_path):
        x=1
        js_file_content = []
        with open(file_path, 'r') as jf:
            for line in jf:
                js_file_content.append(line.rstrip())
        js_element = Script(internal=js_file_content)
        self.add_body_element(js_element)
        return self


