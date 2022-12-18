from phtml.classes.base import Base


class Link(Base):
    def __init__(
        self,
        download=None,
        href=None,
        hreflang=None,
        media=None,
        ping=None,
        referrerpolicy=None,
        rel=None,
        target=None,
        type=None,
        internal=None
    ):
        super().__init__(internal=internal)
        self.start_string = 'a'
        self.end_string = 'a'
        self.attributes['href'] = '#'

        if download is not None:
            self.attributes['download'] = download

        if href is not None:
            self.attributes['href'] = href

        if hreflang is not None:
            self.attributes['hreflang'] = hreflang

        if media is not None:
            self.attributes['media'] = media

        if ping is not None:
            self.attributes['ping'] = ping

        if referrerpolicy is not None:
            self.attributes['referrerpolicy'] = referrerpolicy

        if rel is not None:
            self.attributes['rel'] = rel

        if target is not None:
            self.attributes['target'] = target

        if type is not None:
            self.attributes['type'] = type
