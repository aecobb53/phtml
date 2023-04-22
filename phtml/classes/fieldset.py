from phtml.classes.base import Base


class Fieldset(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'fieldset'
        self.end_string = 'fieldset'


class Legend(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'legend'
        self.end_string = 'legend'
