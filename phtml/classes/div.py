from phtml.classes.base import Base


class Div(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'div'
        self.end_string = 'div'
