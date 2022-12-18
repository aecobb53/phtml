from phtml.classes.text_format import TextFormat

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
        styles = []
        if not isinstance(style_obj, list):
            style_obj = [style_obj]
        for obj in style_obj:
            self.attributes['style'].append(obj)
            # if isinstance(style_obj, dict):
            #     self.attributes['style'].update(style_obj)
            # else:
            #     self.attributes['style'].
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
                style = []
                for att in att_data:
                    if isinstance(att, dict):
                        for key, value in att.items():
                            style.append(f"{key}: {value};")
                    else:
                        style.append(att)
                details[0] += f' style="{" ".join(style)}"'
            elif not isinstance(att_data, list):
                details [0] += f' {attribute}="{att_data}"'
            else:
                details [0] += f' {attribute}="{" ".join(att_data)}"'
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
