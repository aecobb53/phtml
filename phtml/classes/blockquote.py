from phtml.classes.base import Base


class Blockquote(Base):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = 'blockquote'
        self.end_string = 'blockquote'
