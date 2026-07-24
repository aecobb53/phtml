"""
document.py

This module provides the Document class for constructing and managing HTML documents programmatically.
It supports adding head and body elements, managing styles and scripts, loading external CSS and JS files,
and customizing indentation for generated HTML output.

Classes:
    Document: Represents an HTML document with methods to manipulate its structure and content.

Usage:
    Instantiate Document, add elements, styles, scripts, and generate HTML output.
"""

import re

from typing import Any

from . import (
    Html,
    Head,
    Body,
    Style,
    Script,
    HyperLink
)


class Document:
    """
    Represents an HTML document.

    Attributes:
        head (Head(Base(object))): The head section of the document.
        body (Body(Base(object))): The body section of the document.
        styles (list): A list to hold style elements.
        scripts (list): A list to hold script elements.
        indent (str): The string used for indentation in the generated HTML.

    Methods:
        add_head_element(obj): Adds an element to the head of the document.
        add_body_element(obj): Adds an element to the body of the document.
        set_indent_width(width): Sets the indentation width for the generated HTML output.
        return_document: Generates the complete HTML document as a string.
        add_style(style_obj): Adds a Style object to the document head.
        add_favicon(image_path): Adds a favicon link to the document head.
        load_css_file(file_path): Loads a CSS file and adds its styles to the document head.
        load_js_file(file_path): Loads a JavaScript file and adds it as a Script element
            to the document body.

    Example:
        doc = Document()
        doc.add_head_element(Title("My Document"))
        doc.add_body_element(Paragraph("Hello, World!"))
        html_output = doc.return_document
    """

    def __init__(self, head: Head = None, body: Body = None, styles: list = [], scripts: list = [], indent: str = '    '):
        self.head = head
        self.body = body

        if not self.head:
            self.head = Head()
        if not self.body:
            self.body = Body()

        self.styles = styles
        self.scripts = scripts
        self.indent = indent

    def add_head_element(self, obj: Any):
        """
        Adds an element to the head of the document.

        Args:
            obj: The element to be added to the head.

        Returns:
            self: Returns the current instance of the document for method chaining.
        """

        self.head.add_element(obj)
        return self

    def add_body_element(self, obj: Any):
        """
        Adds an element to the body of the document.

        Args:

            obj: The element to be added to the body.

        Returns:
            self: Returns the current instance of the document for method chaining.
        """

        self.body.add_element(obj)
        return self

    def set_indent_width(self, width=4):
        """
        Sets the indentation width for the generated HTML output.

        Args:
            width (int): The number of spaces for indentation. Default is 4.

        Returns:
            self: Returns the current instance of the document for method chaining.
        """

        self.indent = ' ' * width
        return self

    @property
    def return_document(self):
        """
        Generates the complete HTML document as a string.

        Returns:
            str: The complete HTML document as a string.
        """

        for style in self.styles:
            self.head.add_global_style(style)
        for script in self.scripts:
            self.body.add_element(script)

        details = []
        details.append('<!DOCTYPE html>')
        html_element = Html(internal=[self.head, self.body])
        details.extend(html_element.return_document)
        return '\n'.join(details)

    def add_style(self, style_obj: Style):
        """
        Adds a Style object to the document head.

        Args:
            style_obj (Style): The Style object to be added.

        Returns:
            self: Returns the current instance of the document for method chaining.
        """

        self.head.add_global_style(style_obj)
        return self

    def add_favicon(self, image_path: str):
        """
        Adds a favicon link to the document head.

        Args:
            image_path (str): The path to the favicon image file.

        Returns:
            None
        """

        favicon = HyperLink(rel='icon', href=image_path, type='image/x-icon')
        self.add_head_element(favicon)

    def load_css_file(self, file_path: str):
        """
        Loads a CSS file from the specified file path,
        parses its content, and adds the styles to the document head.

        Args:
            file_path (str): The path to the CSS file to be loaded.

        Returns:
            self: Returns the current instance of the document for method chaining.
        """

        with open(file_path, 'r') as cf:
            css_file_content = cf.read()
        css_elements = re.findall(r'([^{]+)\{([^}]+)\}', re.sub(r'/\*.*?\*/', '', css_file_content, flags=re.DOTALL))
        for element in css_elements:
            selector = element[0].strip()
            styles = element[1].strip().split(';')
            style_details = {}
            for style in styles:
                if style.strip() == '':
                    continue
                key, value = style.split(':')
                style_details[key.strip()] = value.strip()
            style_obj = Style(style_details=style_details, name=selector)
            self.add_style(style_obj)
        return self

    def load_js_file(self, file_path: str):
        """
        Loads a JavaScript file from the specified file path,
        and adds it as a Script element to the document body.

        Args:
            file_path (str): The path to the JavaScript file to be loaded.

        Returns:
            self: Returns the current instance of the document for method chaining.
        """

        js_file_content = []
        with open(file_path, 'r') as jf:
            for line in jf:
                js_file_content.append(line.rstrip())
        js_element = Script(internal=js_file_content)
        self.add_body_element(js_element)
        return self
