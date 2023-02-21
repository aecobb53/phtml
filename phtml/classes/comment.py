from phtml.classes.base import Base


class Comment(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = '!--'
        self.end_string = '--'
