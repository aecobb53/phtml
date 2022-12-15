from phtml.classes.base import Base
from phtml.classes.text_format import TextFormat
from phtml.classes.html_list import HtmlList, HtmlListItem

class Document:
    def __init__(self):
        self.head = []
        self.body = []
        self.styles = []
        self.scripts = []
        self.contents = []
        self.indent = '    '

    def add_head_item(self, obj):
        self.body.append(obj)

    def add_body_item(self, obj):
        self.body.append(obj)

    def add_contents(self, obj):
        self.contents.append(obj)

    @property
    def return_document(self):
        details = []
        details.append('<!DOCTYPE html>')
        details.append('<head>')
        for head_item in self.head:
            for line in head_item:
                details.append(self.indent + line.return_document)
        details.append('</head>')
        details.append('<body>')
        for body_item in self.body:
            if isinstance(body_item, TextFormat):
                details.append(f"{self.indent}{body_item.return_content}")
            elif isinstance(body_item, Base):
                for line in body_item.return_document:
                    details.append(f"{self.indent}{line}")
            else:
                details.append(body_item)
        if self.styles:
            style_details = []
            style_details.append('<style>')
            for class_obj in self.styles:
                for class_name, class_details in class_obj.items():
                    style = [f'{self.indent}{class_name} ' + '{']
                    deets = []
                    if isinstance(class_details, list):
                        for cd in class_details:
                            deets.extend([f"{k}: {v};" for k, v in cd.items()])
                    else:
                        deets.extend([f"{k}: {v};" for k, v in class_details.items()])
                    if len(deets) < 1:
                        style[0] += '}'
                    if len(deets) == 1:
                        style[0] += deets[0] + '}'
                    else:
                        style.extend([f"{self.indent * 2}{d}" for d in deets])
                        style.append(self.indent + '}')
                    style_details.extend(style)
            style_details.append('</style>')
            for line in style_details:
                details.append(f"{self.indent}{line}")

            # if isinstance(body_item, str):
            #     details.append(f"{self.indent}{body_item}")
            # for line in body_item.return_document:
            #     details.append(f"{self.indent}{line}")
        details.append('</body>')
        return '\n'.join(details)
