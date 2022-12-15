from phtml.classes.base import Base


class Blockquote(Base):
    def __init__(self):
        super().__init__()
        self.start_string = 'blockquote'
        self.end_string = 'blockquote'
