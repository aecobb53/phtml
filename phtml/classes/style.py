class Style:
    def __init__(self, style_details, name=None):
        self.name = name
        self.styles = style_details
        self.indent = '    '

    @property
    def return_content(self):
        if len(self.styles) <= 1:
            return [self.return_string_version]
        style_l = [self.name + ' {']
        for key, value in self.styles.items():
            style_l.append(f"{self.indent}{key}: {value};")
        style_l.append('}')
        return style_l

    @property
    def return_string_version(self):
        if self.name is None:
            style = '{'
        else:
            style = self.name + ' {'
        style += ' '.join([f'{k}: {v};' for k, v in self.styles.items()])
        style += '}'
        return style

    # @property
    # def return_object_version(self):
    #     content = ';'.join([f'{k}:{v}' for k, v in self.styles.items()])
    #     style = f'style="{content}"'
    #     return style


# descendant
# child
# adjacent
# general
