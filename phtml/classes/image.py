from phtml.classes.base import Base


class Image(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'img'
        self.end_string = False
        self.attributes['src'] = '#'

    def add_src(self, path):
        self.attributes['src'] = path

    def add_alt(self, text):
        self.attributes['alt'] = text
