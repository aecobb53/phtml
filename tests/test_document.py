from phtml.document import Document
from phtml.classes.header import Header
from phtml.classes.div import Div
from phtml.classes.paragraph import Paragraph
from phtml.classes.link import Link
from phtml.classes.hyper_link import HyperLink
from phtml.classes.image import Image
from phtml.classes.blockquote import Blockquote
from phtml.classes.html_list import HtmlList, HtmlListItem
from phtml.classes.text_format import (
    TextFormat,
    LineBreak,
    Bold,
    Strong,
    Italic,
    Emphasized,
    Marked,
    Smaller,
    Deleted,
    Inserted,
    Subscript,
    Superscript,
    Emoji,
)
from phtml import Style

from unittest import TestCase
import pytest


def test_empty():
    doc = Document()
    expected = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n</body>\n</html>'
    actual = doc.return_document
    assert actual == expected

def test_simple_objects():
    doc = Document()
    doc.add_body_element(Header(1))
    doc.add_body_element(Div())
    doc.add_body_element(Paragraph())
    doc.add_body_element(Link())
    doc.add_body_element(Image())
    doc.add_body_element(Blockquote())
    li = HtmlList()
    li.add_element(HtmlListItem('one'))
    li.add_element(HtmlListItem('two'))
    doc.add_body_element(li)

    item = HtmlList()
    item.add_element(HtmlListItem('simple string'))
    item.add_element(HtmlListItem(123))
    item.add_element(HtmlListItem(Div()))
    item.add_element(HtmlListItem(Paragraph()))
    item.add_element(HtmlListItem(Link()))
    item.add_element(HtmlListItem(Image()))
    item.add_element(HtmlListItem(Blockquote()))
    item.add_element(HtmlListItem(Bold('test')))
    item.add_element(HtmlListItem(Strong('test')))
    item.add_element(HtmlListItem(Italic('test')))
    item.add_element(HtmlListItem(Emphasized('test')))
    item.add_element(HtmlListItem(Marked('test')))
    item.add_element(HtmlListItem(Smaller('test')))
    item.add_element(HtmlListItem(Deleted('test')))
    item.add_element(HtmlListItem(Inserted('test')))
    item.add_element(HtmlListItem(Subscript('test')))
    item.add_element(HtmlListItem(Superscript('test')))
    item.add_element(HtmlListItem(Emoji('emojicode')))
    doc.add_body_element(item)

    expected = []
    with open('tests/resources/document_simple_objects.html', 'r') as tf:
        expected = tf.read()
    actual = doc.return_document
    assert actual == expected


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
