from phtml.classes.base import Base


class Body(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'body'
        self.end_string = 'body'
