from phtml.classes.base import Base


class Form(Base):
    def __init__(
            self,
            action=None,
            autocomplete=None,
            enctype=None,
            method=None,
            name=None,
            novalidate=None,
            rel=None,
            target=None,
            internal=None,
            **kwargs
        ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'form'
        self.end_string = 'form'

        if action is not None:
            self.attributes['action'] = action

        if autocomplete is not None:
            self.attributes['autocomplete'] = autocomplete

        if enctype is not None:
            self.attributes['enctype'] = enctype

        if method is not None:
            self.attributes['method'] = method

        if name is not None:
            self.attributes['name'] = name

        if novalidate is not None:
            if novalidate:
                self.attributes['novalidate'] = None

        if rel is not None:
            self.attributes['rel'] = rel

        if target is not None:
            self.attributes['target'] = target
