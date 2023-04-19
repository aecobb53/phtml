from phtml.classes.base import Base


class Input(Base):
    def __init__(
        self,
        internal=None,
        action
        type
        **kwargs
    ):
        super().__init__(internal=internal, **kwargs)
        self.start_string = 'input'
        self.end_string = ''

input - Created

label
select
option
    outgroup
textarea
fieldset
    legend
datalist
output


button - Created
