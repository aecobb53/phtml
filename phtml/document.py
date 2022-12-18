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
                details.append(self.indent + line)
        details.append('</body>')
        details.append('</html>')
        return '\n'.join(details)

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
                details.append(item)
        return details

    def creatre_styles_list(self):
        details = []
        details.append('<style>')
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
                details.extend(style)
        details.append('</style>')
        return details

