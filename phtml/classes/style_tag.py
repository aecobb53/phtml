from phtml.classes.base import Base


class StyleTag(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'style'
        self.end_string = 'style'
