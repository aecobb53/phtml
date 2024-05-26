from phtml.classes.base import Base


class Meta(Base):
    def __init__(self, **kwargs):
        if 'internal' in kwargs:
            kwargs.pop('internal')
        super().__init__(**kwargs)
        self.start_string = 'meta'
        self.end_string = None
