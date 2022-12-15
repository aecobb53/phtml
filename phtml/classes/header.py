from phtml.classes.base import Base


class Header(Base):
    def __init__(self, level, content=None):
        super().__init__()
        self.start_string = f'h{level}'
        self.end_string = f'h{level}'
        if content:
            self.internal.append(content)
