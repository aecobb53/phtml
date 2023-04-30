from phtml.classes.base import Base


class Select(Base):
    def __init__(
            self,
            autofocus=None,
            disabled=None,
            form=None,
            multiple=None,
            name=None,
            required=None,
            size=None,
            internal=None,
            **kwargs
        ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'select'
        self.end_string = 'select'

        if autofocus is not None:
            self.attributes['autofocus'] = autofocus

        if disabled is not None:
            if disabled:
                self.attributes['disabled'] = None

        if form is not None:
            self.attributes['form'] = form

        if multiple is not None:
            self.attributes['multiple'] = multiple

        if name is not None:
            self.attributes['name'] = name

        if required is not None:
            if required:
                self.attributes['required'] = None

        if size is not None:
            self.attributes['size'] = size
