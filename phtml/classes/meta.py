from phtml.classes.base import Base


class Meta(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'meta'
        self.end_string = False
