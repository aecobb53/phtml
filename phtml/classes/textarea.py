from phtml.classes.base import Base


class Textarea(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'textarea'
        self.end_string = 'textarea'
