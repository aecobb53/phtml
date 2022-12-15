from phtml.classes.base import Base


class Image(Base):
    def __init__(self):
        super().__init__()
        self.start_string = 'img'
        self.end_string = False
        self.attributes['src'] = '#'
        self.attributes['alt'] = False

        # width
        # height

    def add_src(self, path):
        self.attributes['src'] = path

    def add_alt(self, text):
        self.attributes['alt'] = text
