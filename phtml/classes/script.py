from phtml.classes.base import Base


class Script(Base):
    def __init__(self, internal=None, async_=None, defer=None, integrity=None, nomodule=None, referrerpolicy=None, src=None, type=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'script'
        self.end_string = 'script'

        if async_ is not None:
            if async_:
                self.attributes['async'] = None

        if defer is not None:
            if defer:
                self.attributes['defer'] = None

        if integrity is not None:
            self.attributes['integrity'] = integrity

        if nomodule is not None:
            self.attributes['nomodule'] = None

        if referrerpolicy is not None:
            self.attributes['referrerpolicy'] = referrerpolicy

        if src is not None:
            self.attributes['src'] = src

        if type is not None:
            self.attributes['type'] = type
