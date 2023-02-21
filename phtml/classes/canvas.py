from phtml.classes.base import Base


class Canvas(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'canvas'
        self.end_string = 'canvas'
