from sys import intern

from numpy import isin
from .text_format import TextFormat
from .style import Style


class Base:
    def __init__(
        self,
        accesskey=None,
        contenteditable=None,
        dir=None,
        draggable=None,
        hidden=None,
        id=None,
        lang=None,
        spellcheck=None,
        tabindex=None,
        title=None,
        translate=None,
        internal=None,
        **kwargs
    ):
        self.attributes = {
            'class': [],
            'style': [],
        }

        if accesskey is not None:
            self.attributes['accesskey'] = accesskey

        if contenteditable is not None:
            self.attributes['contenteditable'] = contenteditable

        if dir is not None:
            self.attributes['dir'] = dir

        if draggable is not None:
            self.attributes['draggable'] = draggable

        if hidden is not None:
            self.attributes['hidden'] = hidden

        if id is not None:
            self.attributes['id'] = id

        if lang is not None:
            self.attributes['lang'] = lang

        if spellcheck is not None:
            self.attributes['spellcheck'] = spellcheck

        if tabindex is not None:
            self.attributes['tabindex'] = tabindex

        if title is not None:
            self.attributes['title'] = title

        if translate is not None:
            self.attributes['translate'] = translate

        self.internal = []
        if internal:
            if isinstance(internal, list):
                self.internal.extend(internal)
            else:
                self.internal.append(internal)
        self.indent = '    '
        self.start_string = None
        self.end_string = None

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
        for attribute, att_data in self.attributes.items():
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
                style += f'{" ".join(style_l)}'
                style += '"'
                details[0] += style
            elif not isinstance(att_data, list):
                details [0] += f' {attribute}="{att_data}"'
            else:
                details [0] += f' {attribute}="{" ".join(att_data)}"'
            # There was an except statement around the if/else block above but i think it was just for testing
        if self.start_string != '!--':
            details[0] += '>'
        if self.internal:
            for internal in self.internal:
                if isinstance(internal, Base):
                    for item in internal.return_document:
                        details.append(self.indent + item)
                elif isinstance(internal, TextFormat):
                    details.append(self.indent + internal.return_content)
                else:
                    try:
                        if internal.strip() == '':
                            continue
                        details.append(self.indent + internal.strip())
                    except:
                        details.append(self.indent + str(internal).strip())
        if self.end_string:
            if self.end_string == '--':
                details.append(f'{self.end_string}>')
            else:
                details.append(f'</{self.end_string}>')
        if len(details) < 3:
            x=1
            if len(details[0]) < 100:
                details = [''.join(details)]
        return details

    @property
    def return_string_version(self):
        details = self.return_document
        return ''.join([l.strip() for l in details])

















# accesskey
# contenteditable
# data-*  -- We could accept kwargs and then if it starts with data- then its one of these objects
# dir
# draggable
# hidden
# id
# lang
# spellcheck
# tabindex
# title
# translate





