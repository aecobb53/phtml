from phtml.classes.base import Base


class Label(Base):
    def __init__(
            self,
            for_id=None,
            form=None,
            internal=None,
            **kwargs
        ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'label'
        self.end_string = 'label'

        if for_id is not None:
            self.attributes['for'] = for_id

        if form is not None:
            self.attributes['form'] = form
