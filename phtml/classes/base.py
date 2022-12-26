from .text_format import TextFormat
from .style import Style


class Base:
    def __init__(self, internal=None):
        self.attributes = {
            'class': [],
            'style': [],
        }
        self.internal = []
        if internal:
            if isinstance(internal, list):
                self.internal.extend(internal)
            else:
                self.internal.append(internal)
        self.indent = '    '
        self.start_string = None
        self.end_string = None

        # self.id

    def add_class(self, class_obj):
        if isinstance(class_obj, list):
            self.attributes['class'].extend(class_obj)
        else:
            self.attributes['class'].append(class_obj)

    def add_style(self, style_obj):
        if not isinstance(style_obj, list):
            style_obj = [style_obj]
        for obj in style_obj:
            self.attributes['style'].append(obj)

    def add_internal(self, obj):
        self.internal.append(obj)

    @property
    def return_document(self):
        details = [f'<{self.start_string}']

        x=1
        for attribute, att_data in self.attributes.items():
            try:
                if not att_data:
                    continue
                if attribute == 'style':
                    style = f' style="'
                    style_l = []
                    for att in att_data:
                        if isinstance(att, Style):
                            style_l.append(att.return_string_version[1:-1])
                        else:
                            for key, value in att.items():
                                style_l.append(f'{key}: {value};')
                            x=1
                    style += f'{" ".join(style_l)}'
                    style += '"'
                    x=1
                    # details[0] += f' style="{" ".join([att.return_string_version[1:-1] for att in att_data])}"'
                    details[0] += style
                elif not isinstance(att_data, list):
                    details [0] += f' {attribute}="{att_data}"'
                else:
                    details [0] += f' {attribute}="{" ".join(att_data)}"'
            except Exception as e:
                e
        details[0] += '>'
        if self.internal:
            for internal in self.internal:
                x=1
                if isinstance(internal, Base):
                    for item in internal.return_document:
                        details.append(self.indent + item)
                elif isinstance(internal, TextFormat):
                    x=1
                    details.append(self.indent + internal.return_content)
                else:
                    try:
                        details.append(self.indent + internal)
                    except:
                        details.append(self.indent + str(internal))
        if self.end_string:
            details.append(f'</{self.end_string}>')
        return details

    @property
    def return_string_version(self):
        details = self.return_document
        return ''.join([l.strip() for l in details])
