from phtml.classes.base import Base


class Head(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'head'
        self.end_string = 'head'
