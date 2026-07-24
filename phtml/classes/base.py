"""
base.py

This module defines the Base class, which serves as the foundational class for all HTML elements in the phtml library.
It provides common functionality for attribute management, internal content handling, and HTML generation.

Classes:
    Base: The main class for representing HTML elements, supporting attributes, styles, classes, and nested content.

Usage:
    The Base class is intended to be subclassed by specific HTML element classes. It offers methods for adding classes,
    styles, and internal elements, as well as generating HTML output and extracting text content.
"""

from typing import Any

from .text_format import TextFormat
from .style import Style



class Base:
    """
    Base class for all elements.
    This class provides common functionality for HTML elements, including
    attribute management, internal content handling, and HTML generation.

    Attributes:
        attributes (dict): A dictionary to hold element attributes.
            attributes['class'] (list): A list to hold class names.
            attributes['style'] (list): A list to hold style definitions.
            attributes[other] : Other attributes as key-value pairs.
        internal (list): A list to hold internal elements or text.
        indent (str): The string used for indentation in the generated HTML.
        start_string (str): The starting tag of the element.
        end_string (str): The ending tag of the element.

    Sub Attributes:
        The following attributes are optional and can be set during initialization but are moved to the attributes dictionary:
            - autofocus
            - accesskey
            - contenteditable
            - dir
            - draggable
            - hidden
            - id
            - lang
            - spellcheck
            - tabindex
            - title
            - translate
            - Any additional attributes passed via kwargs

    Methods:
        add_class(class_obj): Adds a class or classes to the element.
        add_style(style_obj): Adds a style attribute to the element.
        add_element(obj): Adds an internal element to the current element.
        return_document: Generates the HTML representation of the element.
        return_string_version: Returns the full HTML string representation of the element.
        text: Returns just the text content of the element, excluding any HTML tags.

    Example:
        div = Div(id="main", class_="container")
        div.add_class(["new-class", "another-class"])
        div.add_style("color: red; font-size: 14px;")
        div.add_element(Paragraph("Hello, World!"))
        html_output = div.return_string_version
    """

    def __init__(
        self,
        autofocus=None,
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

        if autofocus is not None:
            if autofocus:
                self.attributes['autofocus'] = None

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

        for key, value in kwargs.items():
            self.attributes[key] = value

        self.internal = []
        if internal is not None:
            if isinstance(internal, list):
                self.internal.extend(internal)
            else:
                self.internal.append(internal)
        self.indent = '    '
        self.start_string = None
        self.end_string = None

    def add_class(self, class_obj):
        """
        `Adds a class or classes to the element.

        Args:
            class_obj (str or list): A string representing a single class name
                                     or a list of class names to be added.

        Returns:
            self: Returns the current instance of the element for method chaining.
        """

        if isinstance(class_obj, list):
            self.attributes['class'].extend(class_obj)
        else:
            self.attributes['class'].append(class_obj)
        return self

    def add_style(self, style_obj: Style | str | list):
        """
        Adds a style attribute to the element.

        Args:
            style_obj (Style or str or list): A Style instance, a string of CSS styles
                                              (e.g., "color: red; font-size: 14px;"),
                                              or a list of such strings or Style instances.

        Returns:
            self: Returns the current instance of the element for method chaining.
        """

        if isinstance(style_obj, str):
            style_obj_list = []
            for obj in style_obj.split(';'):
                if obj != '':
                    obj = obj.strip()
                    k, v = obj.split(':')
                    style_obj_list.append({k :v})
            style_obj = style_obj_list
        if not isinstance(style_obj, list):
            style_obj = [style_obj]
        for obj in style_obj:
            self.attributes['style'].append(obj)
        return self

    def add_element(self, obj: Any):
        """
        Adds an internal element to the current element.

        Args:
            obj: The internal element to be added. Can be a string, another Base instance,
                    or a TextFormat instance.

        Returns:
            self: Returns the current instance of the element for method chaining.
        """

        self.internal.append(obj)
        return self

    @property
    def return_document(self):
        """
        Generates the HTML representation of the element, including tags,
        attributes, and internal content.

        Returns:
            list: A list of strings representing the HTML lines of the element.
        """

        details = [f'<{self.start_string}']
        for attribute, att_data in self.attributes.items():
            if attribute == 'class':
                if not att_data:
                    continue
                details[0] += f' class="{" ".join(att_data)}"'
            elif attribute == 'style':
                if not att_data:
                    continue
                style = f' style="'
                style_l = []
                for att in att_data:
                    if isinstance(att, Style):
                        style_item = att.return_string_version[:-1].split('{')[-1]
                        style_l.append(style_item)
                    else:
                        for key, value in att.items():
                            style_l.append(f'{key}: {value};')
                style += f'{" ".join(style_l)}'
                style += '"'
                details[0] += style
            elif not isinstance(att_data, list):
                if att_data is None:
                    details [0] += f' {attribute}'
                else:
                    details [0] += f' {attribute}="{att_data}"'
            else:
                details [0] += f' {attribute}="{" ".join(att_data)}"'
        if self.start_string != '!--':
            details[0] += '>'
        if self.internal:
            for internal in self.internal:
                if isinstance(internal, Base):
                    for item in internal.return_document:
                        details.append(self.indent + item)
                elif isinstance(internal, Style):
                    for item in internal.return_content:
                        details.append(self.indent + item)
                elif isinstance(internal, TextFormat):
                    details.append(self.indent + internal.return_content)
                else:
                    try:
                        if self.start_string == 'script':
                            # Special case
                            details.append(self.indent + internal)
                        else:
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
        if sum([len(item) for item in details]) <= 50 or len(details) < 3:
            for internal_index in range(len(details[1:-1])):
                # Need to remove the indentation
                internal_element = details[internal_index + 1]
                details[internal_index + 1] = internal_element[len(self.indent):]
            details = [''.join(details)]
        return details

    @property
    def return_string_version(self):
        """
        Returns the full HTML string representation of the element,
        including tags and attributes on one line.

        Returns:
            str: The full HTML string representation of the element.
        """

        details = self.return_document
        return ''.join([l.strip() for l in details])

    @property
    def text(self):
        """
        Returns just the text content of the element, excluding any HTML tags.

        Returns:
            str: The text content of the element.
        """

        text_l = []
        for item in self.internal:
            if not isinstance(item, (Base, TextFormat)):
                text_l.append(item)
        return '\n'.join(text_l)
