from phtml.classes.base import Base


class Select(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'select'
        self.end_string = 'select'
