from phtml.classes.base import Base


class Textarea(Base):
    def __init__(
            self,
            autofocus,
            cols=None,
            dirname=None,
            disabled=None,
            form=None,
            maxlength=None,
            name=None,
            placeholder=None,
            readonly=None,
            required=None,
            rows=None,
            wrap=None,
            soft=None,
            internal=None,
            **kwargs,
        ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'textarea'
        self.end_string = 'textarea'


        if autofocus:
            if autofocus:
                self.attributes['autofocus'] = None

        if cols:
            self.attributes['cols'] = cols

        if dirname:
            self.attributes['dirname'] = dirname

        if disabled:
            if disabled:
                self.attributes['disabled'] = None

        if form:
            self.attributes['form'] = form

        if maxlength:
            self.attributes['maxlength'] = maxlength

        if name:
            self.attributes['name'] = name

        if placeholder:
            self.attributes['placeholder'] = placeholder

        if readonly:
            if readonly:
                self.attributes['readonly'] = None

        if required:
            if required:
                self.attributes['required'] = None

        if rows:
            self.attributes['rows'] = rows

        if wrap:
            self.attributes['wrap'] = wrap

        if soft:
            self.attributes['soft'] = soft



