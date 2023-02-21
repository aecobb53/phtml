from phtml.classes.base import Base

class Paragraph(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'p'
        self.end_string = 'p'
