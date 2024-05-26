from phtml.classes.base import Base


class Html(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'html'
        self.end_string = 'html'
