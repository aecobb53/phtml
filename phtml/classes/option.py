from phtml.classes.base import Base


class Option(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'option'
        self.end_string = 'option'
