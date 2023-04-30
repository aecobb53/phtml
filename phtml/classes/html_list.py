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
        content=None,
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
        x=1
        if self.content is None:
            if self.internal is None:
                self.content = ''
            else:
                content = []
                for internal in self.internal:
                    content.append(internal)
                self.content = content
        if not isinstance(self.content, list):
            self.content = [self.content]
        if self.list_item:
            details = ['<li>']
            for content in self.content:
                if isinstance(content, Base):
                    for line in content.return_document:
                        details.append(f"{self.indent}{line}")
                elif isinstance(content, TextFormat):
                    details.append(f"{self.indent}{content.return_content}")
                else:
                    details.append(f"{self.indent}{content}")
            details.append('</li>')
        elif self.list_description:
            details = ['<dl>']
            for content in self.content:
                if isinstance(content, Base):
                    for line in content.return_document:
                        details.append(f"{self.indent}{line}")
                elif isinstance(content, TextFormat):
                    details.append(f"{self.indent}{content.return_content}")
                else:
                    details.append(f"{self.indent}{content}")
            details.append('</dl>')
        elif self.term_description:
            details = ['<dt>']
            for content in self.content:
                if isinstance(self.content, Base):
                    for line in content.return_document:
                        details.append(f"{self.indent}{line}")
                elif isinstance(content, TextFormat):
                    details.append(f"{self.indent}{content.return_content}")
                else:
                    details.append(f"{self.indent}{content}")
            details.append('</dt>')
        elif self.term_in_description_list:
            details = ['<dd>']
            for content in self.content:
                if isinstance(content, Base):
                    for line in content.return_document:
                        details.append(f"{self.indent}{line}")
                elif isinstance(content, TextFormat):
                    details.append(f"{self.indent}{content.return_content}")
                else:
                    details.append(f"{self.indent}{content}")
            details.append('</dd>')
        return details
