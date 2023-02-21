from phtml.classes.base import Base


class IFrame(Base):
    def __init__(
        self,
        src=None,
        title=None,
        height=None,
        width=None,
        border=None,
        internal=None,
        **kwargs
    ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'iframe'
        self.end_string = 'iframe'

        if src is not None:
            self.attributes['src'] = src

        if title is not None:
            self.attributes['title'] = title

        if height is not None:
            self.attributes['height'] = height

        if width is not None:
            self.attributes['width'] = width

        if border is not None:
            self.attributes['border'] = border
