from hashlib import new
from phtml.classes.base import Base


class StyleTag(Base):
    def __init__(self, internal=None, name=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'style'
        self.end_string = 'style'

        self.name = name

    @property
    def return_document(self):
        details = super().return_document
        if self.name:
            inner_content = details[1:-1]
            new_inner_content = [f"{self.indent}{self.name} {{"]
            for item in inner_content:
                new_items = [i.strip() for i in item.split(';') if i.strip() != '']
                for i in new_items:
                    new_inner_content.append(f"{self.indent*2}{i};")
            new_inner_content.append(f"{self.indent}}}")

            details[1:-1] = new_inner_content
        return details
