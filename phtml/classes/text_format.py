class TextFormat:
    def __init__(self, internal=None):
        self.start_string = None
        self.end_string = None
        self.internal = internal

    @property
    def return_content(self):
        if self.start_string is not None:
            details = f'{self.start_string}'
        else:
            details = ''
        if self.internal is not None:
            details += f'{self.internal}'
        if self.end_string is not None:
            details += f'{self.end_string}'
        return details


class LineBreak(TextFormat):
    def __init__(self):
        super().__init__()
        self.start_string = '<br>'
        self.end_string = None


class Bold(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<b>'
        self.end_string = '</b>'


class Strong(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<strong>'
        self.end_string = '</strong>'


class Italic(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<i>'
        self.end_string = '</i>'


class Emphasized(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<em>'
        self.end_string = '</em>'


class Marked(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<mark>'
        self.end_string = '</mark>'


class Smaller(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<small>'
        self.end_string = '</small>'


class Deleted(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<del>'
        self.end_string = '</del>'


class Inserted(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<ins>'
        self.end_string = '</ins>'


class Subscript(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<sub>'
        self.end_string = '</sub>'


class Superscript(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
        self.start_string = '<sup>'
        self.end_string = '</sup>'


class Emoji(TextFormat):
    def __init__(self, internal=None):
        super().__init__(internal=internal)
