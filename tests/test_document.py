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
    expected = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n</body>\n</html>'
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

    ####doc.add_body_element(HyperLink(internal='hyperlink test', href='https://www.google.com'))
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
    # print(content.__dict__)
    # body = [el for el in content.body if isinstance(el, Base)]
    # body = content.body
    print('BACK IN TEST FILE')
    print(content)
    body = []
    for el in content.body:
        if isinstance(el, Base):
            body.append(el)
        elif isinstance(el, str) and el.strip() != '':
            body.append(el)
    for index, el in enumerate(body):
        if type(el) != type(doc.body[index]):
            print('')
            print(f"-{el}-")
            print(f'Expected type: {type(doc.body[index])}')
            print(f'Got type: {type(el)}')
            print('')
            print('Expected details')
            print(f"[{doc.body[index].__dict__}]")
            print('Got details')
            try:
                print(f"[{el.__dict__}]")
            except:
                print(f"[{el}]")
        assert type(doc.body[index]) == type(el)
        
    1/0



# def test_styles():
#     doc = Document()
#     div = Div()
#     div.add_class('class1')
#     div.add_class('class2')
#     div.add_class('class3')
#     doc.body.append(div)

#     doc.styles.append({'class1': {'display': 'inline-block'}})
#     doc.styles.append({'class2': [
#         {'border-style': 'solid'},
#     ]})
#     doc.styles.append({'class3': [
#         {'min-width': '300px'},
#         {'max-width': '350px'},
#     ]})
#     expected = []
#     with open('tests/resources/document_styles.html', 'r') as tf:
#         for line in tf.readlines():
#             expected.append(line)
#     expected = "".join(expected)
#     actual = doc.return_document
#     assert actual == expected

# def test_real_file():
#     doc = Document()
#     doc.body.append(Header(1, 'Example File'))
#     doc.body.append(Header(2, 'Content header'))

#     main_div = Div()
#     color_list_1 = ['red', 'green', 'blue', 'purple', 'cyan']
#     color_list_2 = ['lightcoral', 'cyan', 'red', 'green', 'purple']
#     for index in range(5):
#         div = Div()
#         div.internal.append(f"Some content {index}")
#         div.add_style(f'background-color: {color_list_1[index]};')
#         div.add_style(f'color: {color_list_2[index]};')
#         div.add_class('class1')
#         div.add_class('class2')
#         main_div.internal.append(div)
#     doc.body.append(main_div)
#     doc.styles.append({
#         'class1': [{'border-style': 'solid'}],
#         'class2': [
#             {'display': 'inline-block'},
#             {'min-width': '300px'},
#             {'max-width': '350px'},
#         ]
#     })
#     content = Paragraph()
#     content.add_class('test1')
#     content.add_style({'text-block': 'centered'})
#     content.internal.append('simple string')
#     content.internal.append(123)
#     content.internal.append(Div())
#     content.internal.append(Paragraph())
#     content.internal.append(Link())
#     content.internal.append(HyperLink())
#     content.internal.append(Image())
#     content.internal.append(Blockquote())
#     content.internal.append(LineBreak())
#     content.internal.append(Bold('test'))
#     content.internal.append(Strong('test'))
#     content.internal.append(Italic('test'))
#     content.internal.append(Emphasized('test'))
#     content.internal.append(Marked('test'))
#     content.internal.append(Smaller('test'))
#     content.internal.append(Deleted('test'))
#     content.internal.append(Inserted('test'))
#     content.internal.append(Subscript('test'))
#     content.internal.append(Superscript('test'))
#     content.internal.append(Emoji('emojicode'))
#     doc.body.append(content)

#     expected = []
#     with open('tests/resources/document_actual_html_page.html', 'r') as tf:
#         for line in tf.readlines():
#             expected.append(line)
#     expected = "".join(expected)
#     actual = doc.return_document
#     assert actual == expected

# ['span.py', 'script.py', 'input.py', 'meta.py', 'noscript.py', 'comment.py', 'svg.py', 'form.py', 'canvas.py', 'iframe.py']
