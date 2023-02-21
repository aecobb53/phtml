from phtml.classes.base import Base


class Noscript(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'noscript'
        self.end_string = 'noscript'
