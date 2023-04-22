from phtml.classes.base import Base


class Datalist(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'datalist'
        self.end_string = 'datalist'
