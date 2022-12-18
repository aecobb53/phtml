from phtml.classes.base import Base


class Header(Base):
    def __init__(self, level, internal=None):
        super().__init__(internal=internal)
        self.start_string = f'h{level}'
        self.end_string = f'h{level}'
        # if content:
        #     self.internal.append(content)
