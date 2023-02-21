from phtml.classes.base import Base


class Header(Base):
    def __init__(self, level, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = f'h{level}'
        self.end_string = f'h{level}'
