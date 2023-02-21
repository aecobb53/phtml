from phtml.classes.base import Base


class Svg(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'svg'
        self.end_string = 'svg'


class SubParameter(Base):
    def __init__(self, start_tag, end_tag=None, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = start_tag
        self.end_string = end_tag
