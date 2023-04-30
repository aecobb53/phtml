from phtml.classes.base import Base


class Option(Base):
    def __init__(
            self,
            disabled=None,
            label=None,
            selected=None,
            value=None,
            internal=None,
            **kwargs
            ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'option'
        self.end_string = 'option'

        if disabled:
            if disabled:
                self.attributes['disabled'] = None
        if label:
            self.attributes['label'] = label
        if selected:
            if selected:
                self.attributes['selected'] = None
        if value:
            self.attributes['value'] = value
