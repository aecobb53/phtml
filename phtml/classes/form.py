from phtml.classes.base import Base


class Form(Base):
    def __init__(self, internal=None, action=None, autocomplete=None, target=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'form'
        self.end_string = 'form'

        if action is not None:
            # URL
            self.attributes['action'] = action

        if autocomplete is not None:
            if autocomplete:
                self.attributes['autocomplete'] = 'on'
            else:
                self.attributes['autocomplete'] = 'off'

        if target is not None:
            if target in ['_blank', '_self', '_parent', '_top']:
                self.attributes['target'] = target


class FormBase(Base):
    def __init__(self, internal=None, form=None, disabled=None, name=None, required=None, **kwargs):
        super().__init__(internal=internal, **kwargs)

        if form is not None:
            self.attributes['form'] = form

        if disabled is not None:
            if disabled:
                self.attributes['disabled'] = None

        if name is not None:
            self.attributes['name'] = name

        if required is not None:
            if required:
                self.attributes['required'] = None


class Textarea(FormBase):
    def __init__(self,
    internal=None,
    cols=None,
    maxlength=None,
    placeholder=None,
    readonly=None,
    rows=None,
    wrap=None,
    **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'textarea'
        self.end_string = 'textarea'

        if cols is not None:
            self.attributes['cols'] = cols

        if maxlength is not None:
            self.attributes['maxlength'] = maxlength

        if placeholder is not None:
            self.attributes['placeholder'] = placeholder

        if readonly is not None:
            if readonly:
                self.attributes['readonly'] = None

        if rows is not None:
            self.attributes['rows'] = rows

        if wrap is not None:
            if wrap in ['hard', 'soft']:
                self.attributes['wrap'] = wrap


class Select(FormBase):
    def __init__(self, internal=None, multiple=None, size=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'select'
        self.end_string = 'select'

        if multiple is not None:
            if multiple:
                self.attributes['multiple'] = None

        if size is not None:
            self.attributes['size'] = size


class Option(FormBase):
    def __init__(self, internal=None, label=None, selected=None, value=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'option'
        self.end_string = 'option'

        if label is not None:
            self.attributes['label'] = label

        if selected is not None:
            if selected:
                self.attributes['selected'] = None

        if value is not None:
            self.attributes['value'] = value


class Optiongroup(FormBase):
    def __init__(self, internal=None, label=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'optgroup'
        self.end_string = 'optgroup'

        if label is not None:
            self.attributes['label'] = label


class Fieldset(FormBase):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'fieldset'
        self.end_string = 'fieldset'


class Label(FormBase):
    def __init__(self, internal=None, for_=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'label'
        self.end_string = 'label'

        if for_ is not None:
            self.attributes['for'] = for_


class Output(FormBase):
    def __init__(self, internal=None, for_=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'output'
        self.end_string = 'output'

        if for_ is not None:
            self.attributes['for'] = for_
