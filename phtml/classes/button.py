from phtml.classes.base import Base


class Button(Base):
    def __init__(
        self,
        internal=None,
        autofocus=None,
        disabled=None,
        form=None,
        formaction=None,
        formenctype=None,
        formmethod=None,
        formnovalidate=None,
        formtarget=None,
        name=None,
        type=None,
        value=None,
    ):
        super().__init__(internal=internal)
        self.start_string = 'button'
        self.end_string = 'button'

        if autofocus is not None:
            self.attributes['autofocus'] = None

        if disabled is not None:
            self.attributes['disabled'] = None

        if form is not None:
            self.attributes['form'] = form

        if formaction is not None:
            self.attributes['formaction'] = formaction

        if formenctype is not None:
            self.attributes['formenctype'] = formenctype

        if formmethod is not None:
            self.attributes['formmethod'] = formmethod

        if formnovalidate is not None:
            self.attributes['formnovalidate'] = formnovalidate

        if formtarget is not None:
            self.attributes['formtarget'] = formtarget

        if name is not None:
            self.attributes['name'] = name

        if type is not None:
            self.attributes['type'] = type

        if value is not None:
            self.attributes['value'] = value
