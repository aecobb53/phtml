from phtml.classes.base import Base


class Input(Base):
    def __init__(self, internal=None, **kwargs):
        internal = None  # There is no internal content for the input tag
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'input'
        self.end_string = None
