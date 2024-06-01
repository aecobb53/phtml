from sys import intern
from phtml import Document
from phtml import HtmlReader
from phtml import Style
from phtml import Base
from phtml import Blockquote
from phtml import Inlinequote
from phtml import Button
from phtml import Canvas
from phtml import Comment
from phtml import Div
from phtml import Form
from phtml import Textarea
from phtml import Select
from phtml import Option
from phtml import Optiongroup
from phtml import Fieldset
from phtml import Label
from phtml import Output
from phtml import Header
from phtml import HtmlList
from phtml import HtmlListItem
from phtml import HyperLink
from phtml import IFrame
from phtml import Image
from phtml import Input
from phtml import Link
from phtml import Meta
from phtml import Noscript
from phtml import Paragraph
from phtml import Script
from phtml import Span
from phtml import Svg
from phtml import TextFormat
from phtml import Table
from phtml import TableRow
from phtml import TableHeader
from phtml import TableData
from phtml import LineBreak
from phtml import Bold
from phtml import Strong
from phtml import Italic
from phtml import Emphasized
from phtml import Marked
from phtml import Smaller
from phtml import Deleted
from phtml import Inserted
from phtml import Subscript
from phtml import Superscript
from phtml import Emoji
from phtml import Title

from unittest import TestCase
import pytest


def test_empty():
    doc = Document()
    expected = '<!DOCTYPE html>\n<html>\n<head></head>\n<body></body>\n</html>'
    actual = doc.return_document
    assert actual == expected

def test_simple_objects():
    doc = Document()
    doc.add_body_element(Div('div test').add_style({'color': 'red'}).add_style({'background': 'green'}).add_class('test').add_class('another-test').add_element(Div()).add_element('A string'))

    doc.add_body_element(Blockquote('blockquote test'))
    doc.add_body_element(Inlinequote('inlinequote test'))
    doc.add_body_element(Canvas('canvas test'))
    doc.add_body_element(Comment())
    doc.add_body_element(Comment('A comment'))
    doc.add_body_element('A generic string')
    doc.add_body_element(Div('div test'))
    form = Form()
    form.add_element(Button('button test'))
    form.add_element(Textarea('textarea test'))
    form.add_element(Select('select test'))
    form.add_element(Option('option test'))
    form.add_element(Optiongroup('optiongroup test'))
    form.add_element(Fieldset('fieldset test'))
    form.add_element(Label('label test'))
    form.add_element(Output('output test'))
    doc.add_body_element(form)

    doc.add_body_element(Header(level=1, internal='header test 1'))
    doc.add_body_element(Header(level=2, internal='header test 2'))
    doc.add_body_element(Header(level=3, internal='header test 3'))
    doc.add_body_element(Header(level=4, internal='header test 4'))
    doc.add_body_element(Header(level=5, internal='header test 5'))
    doc.add_body_element(Header(level=6, internal='header test 6'))

    ordered_html_list = HtmlList(ordered=True)
    ordered_html_list.add_element(HtmlListItem('ordered list item 1'))
    doc.add_body_element(ordered_html_list)

    unordered_html_list = HtmlList(ordered=False)
    unordered_html_list.add_element(HtmlListItem('unordered list item 1'))
    doc.add_body_element(unordered_html_list)

    doc.add_body_element(HyperLink(href='https://www.google.com'))
    doc.add_body_element(IFrame(src='https://www.google.com'))
    doc.add_body_element(Input('input test'))
    doc.add_body_element(Link('link test'))
    doc.add_body_element(Meta())
    doc.add_body_element(Noscript('noscript test'))
    doc.add_body_element(Paragraph('paragraph test'))
    doc.add_body_element(Script())
    doc.add_body_element(Script('script-test'))
    doc.add_body_element(Span('span test'))
    doc.add_body_element(Svg('svg test'))

    table = Table()
    header_row = TableRow()
    header_row.add_element(TableHeader('table header test'))
    data_row = TableRow()
    data_row.add_element(TableData('table data test'))
    table.add_element(header_row)
    table.add_element(data_row)
    doc.add_body_element(table)

    paragraph = Paragraph()
    paragraph.add_element(LineBreak())
    paragraph.add_element(Bold('bold test'))
    paragraph.add_element(Strong('strong test'))
    paragraph.add_element(Italic('italic test'))
    paragraph.add_element(Emphasized('emphasized test'))
    paragraph.add_element(Marked('marked test'))
    paragraph.add_element(Smaller('smaller test'))
    paragraph.add_element(Deleted('deleted test'))
    paragraph.add_element(Inserted('inserted test'))
    paragraph.add_element(Subscript('subscript test'))
    paragraph.add_element(Superscript('superscript test'))
    paragraph.add_element(Emoji('emoji test'))
    doc.add_body_element(Title('title test'))
    doc.add_body_element(paragraph)



    expected = []
    saved_file_path = 'tests/resources/document_simple_objects.html'
    with open(saved_file_path, 'w') as tf:
        tf.write(doc.return_document)
    with open(saved_file_path, 'r') as tf:
        expected = tf.read()
    actual = doc.return_document
    assert actual == expected

    # Parse that output
    hr = HtmlReader()
    content = hr.read_file(saved_file_path)[0]
    print('BACK IN TEST FILE')
    print(content)
    print(f"html: {str(content.html)[:50]}")
    print(f"head: {str(content.head)[:50]}")
    print(f"body: {str(content.body)[:50]}")
    print(type(content.body))
    body = []
    for el in content.html.internal[1].internal:
        if isinstance(el, Base):
            body.append(el)
        elif isinstance(el, str) and el.strip() != '':
            body.append(el)
    for index, el in enumerate(body):
        if type(el) != type(doc.body.internal[index]):
            print('')
            print(f"-{el}-")
            print(f'Expected type: {type(doc.body.internal[index])}')
            print(f'Got type: {type(el)}')
            print('')
            print('Expected details')
            print(f"[{doc.body.internal[index].__dict__}]")
            print('Got details')
