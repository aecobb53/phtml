from phtml.classes.base import Base


class Button(Base):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = 'button'
        self.end_string = 'button'
