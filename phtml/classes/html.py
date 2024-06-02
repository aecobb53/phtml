from phtml.classes.base import Base


class Html(Base):
    def __init__(self, internal=None, **kwargs):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'html'
        self.end_string = 'html'

    @property
    def return_document(self):
        """
        I dont want the full block indented unnecessarily
        """
        details = super().return_document
        for i in range(len(details)):
            if i > 0 and i < len(details) - 1:
                details[i] = f"{details[i][4:]}"
        return details
