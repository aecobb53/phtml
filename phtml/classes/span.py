from phtml.classes.base import Base


class Span(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'span'
        self.end_string = 'span'
