from phtml.classes.base import Base


class HyperLink(Base):
    def __init__(
        self,
        crossorigin=None,
        href=None,
        hreflang=None,
        media=None,
        referrerpolicy=None,
        rel=None,
        sizes=None,
        title=None,
        type=None,
    ):
        super().__init__()
        self.start_string = 'link'
        self.end_string = 'link'
        self.attributes['href'] = '#'

        if crossorigin is not None:
            self.attributes['crossorigin'] = crossorigin

        if href is not None:
            self.attributes['href'] = href

        if hreflang is not None:
            self.attributes['hreflang'] = hreflang

        if media is not None:
            self.attributes['media'] = media

        if referrerpolicy is not None:
            self.attributes['referrerpolicy'] = referrerpolicy

        if rel is not None:
            self.attributes['rel'] = rel

        if sizes is not None:
            self.attributes['sizes'] = sizes

        if title is not None:
            self.attributes['title'] = title

        if type is not None:
            self.attributes['type'] = type
