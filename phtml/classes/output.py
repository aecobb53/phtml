from phtml.classes.base import Base


class Output(Base):
    def __init__(
            self,
            for_id=None,
            form=None,
            name=None,
            internal=None,
            **kwargs
        ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'output'
        self.end_string = 'output'

        if for_id:
            self.attributes['for'] = for_id

        if form:
            self.attributes['form'] = form

        if name:
            self.attributes['name'] = name
