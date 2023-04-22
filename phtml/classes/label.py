from phtml.classes.base import Base


class Label(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'label'
        self.end_string = 'label'
