from phtml.classes.base import Base


class Link(Base):
    def __init__(self):
        super().__init__()
        self.start_string = 'a'
        self.end_string = 'a'
        self.attributes['href'] = '#'

    def add_href(self, link):
        self.attributes['href'] = link
