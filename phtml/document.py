from . import Base
from . import Html
from . import Head
from . import Body
from . import TextFormat
from . import Style


class Document:
    def __init__(self, html: Html = None, head: Head = None, body: Body = None, **kwargs):
        self.html = html
        self.head = head
        self.body = body
        if not self.html and not self.head and not self.body:
            self.html = Html(
                internal=[Head(), Body()]
            )
        if not self.html and not self.head:
            self.head = Head()
        if not self.html and not self.body:
            self.body = Body()
        self.styles = []
        self.scripts = []
        self.indent = '    '

    def add_head_element(self, obj):
        if self.html:
            self.html.internal[0].add_element(obj)
        else:
            self.head.add_element(obj)
        return self

    def add_body_element(self, obj):
        if self.html:
            self.html.internal[1].add_element(obj)
        else:
            self.body.add_element(obj)
        return self

    def set_indent_width(self, width=4):
        self.indent = ' ' * width
        return self

    @property
    def return_document(self):
        details = []
        details.append('<!DOCTYPE html>')
        if self.html:
            details.extend(self.html.return_document)
        else:
            details.append('<html>')
            details.extend(self.head.return_document)
            details.extend(self.body.return_document)
            details.append('</html>')
        return '\n'.join(details)

    def add_style(self, style_obj):
        if not isinstance(style_obj, list):
            style_obj = [style_obj]
        for obj in style_obj:
            if self.html:
                self.html.internal[1].add_style(obj)
            else:
                self.body.add_style(obj)
            # self.styles.append(obj)
        return self

    # def create_details_list(self, lst):
    #     details = []
    #     for item in lst:
    #         x=1
    #         if isinstance(item, TextFormat):
    #             details.append(f"{self.indent}{item.return_content}")
    #         elif isinstance(item, Base):
    #             for line in item.return_document:
    #                 details.append(f"{self.indent}{line}")
    #         else:
    #             if item.strip() == '':
    #                 continue
    #             details.append(f"{self.indent}{item}")
    #     return details

    # def create_styles_list(self):
    #     details = []
    #     details.append('<style>')
    #     for style in self.styles:
    #         if not isinstance(style, Style):
    #             details.append(style.return_string_version)
    #             continue
    #         for line in style.return_content:
    #             details.append(f"{self.indent}{line}")
    #     details.append('</style>')
    #     return details
