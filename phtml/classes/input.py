from phtml.classes.base import Base


class Input(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'input'
        self.end_string = ''
