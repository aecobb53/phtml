from phtml.classes.base import Base


class Form(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'form'
        self.end_string = 'form'
