from phtml.classes.base import Base


class Blockquote(Base):
    def __init__(self, internal=None, cite=None):
        super().__init__(internal=internal)
        self.start_string = 'blockquote'
        self.end_string = 'blockquote'
        if cite:
            self.attributes['cite'] = cite


class Inlinequote(Base):
    def __init__(self, internal=None, cite=None):
        super().__init__(internal=internal)
        self.start_string = 'q'
        self.end_string = 'q'
        if cite:
            self.attributes['cite'] = cite
