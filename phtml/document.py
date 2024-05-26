from phtml.classes.base import Base
from phtml.classes.text_format import TextFormat
from phtml.classes.style import Style


class Document:
    def __init__(self, **kwargs):
        self.head = []
        self.body = []
        self.styles = []
        self.scripts = []
        self.indent = '    '

    def add_head_element(self, obj):
        self.body.append(obj)
        return self

    def add_body_element(self, obj):
        self.body.append(obj)
        return self

    def set_indent_width(self, width=4):
        self.indent = ' ' * width
        return self

    @property
    def return_document(self):
        details = []
        details.append('<!DOCTYPE html>')
        details.append('<html>')
        details.append('<head>')
        for line in self.create_details_list(lst=self.head):
            details.append(line)
        details.append('</head>')
        details.append('<body>')
        for line in self.create_details_list(lst=self.body):
            details.append(line)
        if self.styles:
            for line in self.creatre_styles_list():
                details.append(f"{self.indent}{line}")
        details.append('</body>')
        details.append('</html>')
        return '\n'.join(details)

    def add_style(self, style_obj):
        if not isinstance(style_obj, list):
            style_obj = [style_obj]
        for obj in style_obj:
            self.styles.append(obj)
        return self

    def create_details_list(self, lst):
        details = []
        for item in lst:
            x=1
            if isinstance(item, TextFormat):
                details.append(f"{self.indent}{item.return_content}")
            elif isinstance(item, Base):
                for line in item.return_document:
                    details.append(f"{self.indent}{line}")
            else:
                if item.strip() == '':
                    continue
                details.append(f"{self.indent}{item}")
        return details

    def creatre_styles_list(self):
        details = []
        details.append('<style>')
        for style in self.styles:
            if not isinstance(style, Style):
                details.append(style.return_string_version)
                continue
            for line in style.return_content:
                details.append(f"{self.indent}{line}")
        details.append('</style>')
        return details
