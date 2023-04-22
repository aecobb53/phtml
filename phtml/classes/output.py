from phtml.classes.base import Base


class Output(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'output'
        self.end_string = 'output'
