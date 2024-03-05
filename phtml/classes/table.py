from phtml.classes.base import Base
from .text_format import TextFormat


class Table(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'table'
        self.end_string = 'table'


class TableRow(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'tr'
        self.end_string = 'tr'


class TableHeader(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'th'
        self.end_string = 'th'


class TableData(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'td'
        self.end_string = 'td'
