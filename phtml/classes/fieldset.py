from phtml.classes.base import Base


class Fieldset(Base):
    def __init__(
            self,
            disabled=None,
            form=None,
            name=None,
            internal=None,
            **kwargs
        ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'fieldset'
        self.end_string = 'fieldset'

        if disabled:
            if disabled:
                self.attributes['disabled'] = None

        if form:
            self.attributes['form'] = form

        if name:
            self.attributes['name'] = name


class Legend(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'legend'
        self.end_string = 'legend'
