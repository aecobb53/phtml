from phtml.classes.base import Base
from .text_format import TextFormat


class HtmlList(Base):
    def __init__(self, ordered=False, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        if ordered:
            self.start_string = 'ol'
            self.end_string = 'ol'
        else:
            self.start_string = 'ul'
            self.end_string = 'ul'


class HtmlListItem(Base):
    def __init__(
        self,
        content,
        indent='    ',
        list_item=None,
        list_description=None,
        term_description=None,
        term_in_description_list=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.content = content
        self.indent = indent
        self.list_item = list_item
        self.list_description = list_description
        self.term_description = term_description
        self.term_in_description_list = term_in_description_list

        if not any([list_item, list_description, term_description, term_in_description_list]):
            self.list_item = True

    @property
    def return_document(self):
        if self.list_item:
            if isinstance(self.content, Base):
                details = ['<li>']
                for line in self.content.return_document:
                    details.append(f"{self.indent}{line}")
                details.append('</li>')
            elif isinstance(self.content, TextFormat):
                details = ['<li>']
                details.append(f"{self.indent}{self.content.return_content}")
                details.append('</li>')
            else:
                details = [f"<li>{self.content}</li>"]
        elif self.list_description:
            if isinstance(self.content, Base):
                details = ['<dl>']
                for line in self.content.return_document:
                    details.append(f"{self.indent}{line}")
                details.append('</dl>')
            elif isinstance(self.content, TextFormat):
                details = ['<dl>']
                for line in self.content.return_content:
                    details.append(f"{self.indent}{line}")
                details.append('</dl>')
            else:
                details = [f"<dl>{self.content}</dl>"]
        elif self.term_description:
            if isinstance(self.content, Base):
                details = ['<dt>']
                for line in self.content.return_document:
                    details.append(f"{self.indent}{line}")
                details.append('</dt>')
            elif isinstance(self.content, TextFormat):
                details = ['<dt>']
                for line in self.content.return_content:
                    details.append(f"{self.indent}{line}")
                details.append('</dt>')
            else:
                details = [f"<dt>{self.content}</dt>"]
        elif self.term_in_description_list:
            if isinstance(self.content, Base):
                details = ['<dd>']
                for line in self.content.return_document:
                    details.append(f"{self.indent}{line}")
                details.append('</dd>')
            elif isinstance(self.content, TextFormat):
                details = ['<dd>']
                for line in self.content.return_content:
                    details.append(f"{self.indent}{line}")
                details.append('</dd>')
            else:
                details = [f"<dd>{self.content}</dd>"]
        return details
