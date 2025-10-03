from phtml.classes.base import Base
from phtml.classes.style_tag import StyleTag


class Head(Base):
    def __init__(self, internal=None, global_styles=[], **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'head'
        self.end_string = 'head'
        self.global_styles = global_styles

    def add_global_style(self, style):
        self.global_styles.append(style)
        return self

    @property
    def return_document(self):
        if self.global_styles:
            global_style = StyleTag(internal=self.global_styles)
            self.add_element(global_style)
        details = super().return_document
        return details
