from phtml.classes.base import Base


class Input(Base):
    def __init__(
        self,
        internal=None,
        accept=None,
        alt=None,
        autocomplete=None,
        autofocus=None,
        checked=None,
        dirname=None,
        disabled=None,
        form=None,
        formaction=None,
        action=None,
        formenctype=None,
        enctype=None,
        formmethod=None,
        method=None,
        formnovalidate=None,
        novalidate=None,
        formtarget=None,
        target=None,
        height=None,
        list=None,
        max=None,
        maxlength=None,
        min=None,
        minlength=None,
        multiple=None,
        name=None,
        pattern=None,
        placeholder=None,
        readonly=None,
        required=None,
        size=None,
        src=None,
        step=None,
        type=None,
        value=None,
        width=None,



        **kwargs
    ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'input'
        self.end_string = ''


        if accept is not None:
            self.attributes['accept'] = accept

        if alt is not None:
            self.attributes['alt'] = alt

        if autocomplete is not None:
            self.attributes['autocomplete'] = autocomplete

        if autofocus is not None:
            if autofocus:
                self.attributes['autofocus'] = None

        if checked is not None:
            if checked:
                self.attributes['checked'] = None

        if dirname is not None:
            self.attributes['dirname'] = dirname

        if disabled is not None:
            if disabled:
                self.attributes['disabled'] = None

        if form is not None:
            self.attributes['form'] = form

        if formaction is not None:
            self.attributes['formaction'] = formaction

        if action is not None:
            self.attributes['action'] = action

        if formenctype is not None:
            self.attributes['formenctype'] = formenctype

        if enctype is not None:
            self.attributes['enctype'] = enctype

        if formmethod is not None:
            self.attributes['formmethod'] = formmethod

        if method is not None:
            self.attributes['method'] = method

        if formnovalidate is not None:
            self.attributes['formnovalidate'] = formnovalidate

        if novalidate is not None:
            self.attributes['novalidate'] = novalidate

        if formtarget is not None:
            self.attributes['formtarget'] = formtarget

        if target is not None:
            self.attributes['target'] = target

        if height is not None:
            self.attributes['height'] = height

        if list is not None:
            self.attributes['list'] = list

        if max is not None:
            self.attributes['max'] = max

        if maxlength is not None:
            self.attributes['maxlength'] = maxlength

        if min is not None:
            self.attributes['min'] = min

        if minlength is not None:
            self.attributes['minlength'] = minlength

        if multiple is not None:
            if multiple:
                self.attributes['multiple'] = None

        if name is not None:
            self.attributes['name'] = name

        if pattern is not None:
            self.attributes['pattern'] = pattern

        if placeholder is not None:
            self.attributes['placeholder'] = placeholder

        if readonly is not None:
            if readonly:
                self.attributes['readonly'] = readonly

        if required is not None:
            if required:
                self.attributes['required'] = None

        if size is not None:
            self.attributes['size'] = size

        if src is not None:
            self.attributes['src'] = src

        if step is not None:
            self.attributes['step'] = step

        if type is not None:
            self.attributes['type'] = type

        if value is not None:
            self.attributes['value'] = value

        if width is not None:
            self.attributes['width'] = width




# input - Created

# label
# select
# option
#     outgroup
# textarea
# fieldset
#     legend
# datalist
# output


# button - Created
