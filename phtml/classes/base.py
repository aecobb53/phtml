from phtml.classes.text_format import TextFormat

class Base:
    def __init__(self):
        self.attributes = {
            'class': [],
            'style': {},
        }
        self.internal = []
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
        # for key, value in style_obj.items():
        #     self.attributes['style'][key] = value
        self.attributes['style'].update(style_obj)
        # if not isinstance(style_obj, list):
        #     self.attributes['style'].extend(style_obj)
        # else:
        #     self.attributes['style'].append(style_obj)
        # if isinstance(style_obj, list):
        #     self.attributes['style'].extend(style_obj)
        # else:
        #     self.attributes['style'].append(style_obj)

    def add_internal(self, obj):
        self.internal.append(obj)

    @property
    def return_document(self):
        details = [f'<{self.start_string}']
        for attribute, att_data in self.attributes.items():
            if not att_data:
                continue
            if attribute == 'style':
                # x=1
                # a = [f'{k}: {v};' for k, v in att_data.items()]
                # b = " ".join([f'{k}: {v};' for k, v in att_data.items()])
                # c = f' style="{" ".join([f"{k}: {v};" for k, v in att_data.items()])}"'
                # x=1
                details[0] += f' style="{" ".join([f"{k}: {v};" for k, v in att_data.items()])}"'
                # x=1
                # for att in att_data:
                #     for name, deets in att.items():
                #         details[0] += f' {attribute}=""'
            elif not isinstance(att_data, list):
                details [0] += f' {attribute}="{att_data}"'
            else:
                details [0] += f' {attribute}="{" ".join(att_data)}"'
        details[0] += '>'
        if self.internal:
            for internal in self.internal:
                if isinstance(internal, TextFormat):
                    x=1
                if isinstance(internal, Base):
                    x=1
                    for item in internal.return_document:
                        details.append(self.indent + item)
                else:
                    x=1
                    details.append(self.indent + internal)
        if self.end_string:
            details.append(f'</{self.end_string}>')
        return details
