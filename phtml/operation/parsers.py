import re

from ..classes.style import Style


def parse_style(style_string):
    style_string = re.sub(r'\/\*[a-zA-Z0-9.,{}()\[\] :;#\%-]+\*/', '', style_string) # Removing comments
    results = style_string.split('}')
    styles = []
    for item in results:
        if item == '':
            continue
        kv = item.split('{')
        kv[-1] = kv[-1].strip()
        if len(kv) == 1:
            name = None
        else:
            name = kv[0].strip()
        style = {}
        for nkv in kv[-1].split(';'):
            nkv = nkv.strip()
            if nkv == '':
                continue
            key, value = nkv.split(':')
            style[key] = value
        styles.append(Style(name=name, style_details=style))
    return styles
