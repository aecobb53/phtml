from phtml.classes.base import Base


class Title(Base):
    def __init__(
        self,
        content=None,
    ):
        super().__init__()
        self.start_string = 'title'
        self.end_string = 'title'
        if content:
            self.internal.append(content)
