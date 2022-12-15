from phtml.classes.base import Base

class Paragraph(Base):
    def __init__(self):
        super().__init__()
        self.start_string = 'p'
        self.end_string = 'p'
