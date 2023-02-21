from phtml.classes.base import Base


class Title(Base):
    def __init__(
        self,
        internal=None,
        **kwargs
    ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'title'
        self.end_string = 'title'
