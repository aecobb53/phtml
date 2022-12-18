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
from unittest import TestCase
import pytest


def test_empty():
    doc = Document()
    expected = '<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n</body>\n</html>'
    actual = doc.return_document
    assert actual == expected

def test_simple_objects():
    doc = Document()
    doc.body.append(Header(1))
    doc.body.append(Div())
    doc.body.append(Paragraph())
    doc.body.append(Link())
    doc.body.append(Image())
    doc.body.append(Blockquote())
    li = HtmlList()
    li.internal.append(HtmlListItem('one'))
    li.internal.append(HtmlListItem('two'))
    doc.body.append(li)

    item = HtmlList()
    item.internal.append(HtmlListItem('simple string'))
    item.internal.append(HtmlListItem(123))
    item.internal.append(HtmlListItem(Div()))
    item.internal.append(HtmlListItem(Paragraph()))
    item.internal.append(HtmlListItem(Link()))
    item.internal.append(HtmlListItem(Image()))
    item.internal.append(HtmlListItem(Blockquote()))
    item.internal.append(HtmlListItem(Bold('test')))
    item.internal.append(HtmlListItem(Strong('test')))
    item.internal.append(HtmlListItem(Italic('test')))
    item.internal.append(HtmlListItem(Emphasized('test')))
    item.internal.append(HtmlListItem(Marked('test')))
    item.internal.append(HtmlListItem(Smaller('test')))
    item.internal.append(HtmlListItem(Deleted('test')))
    item.internal.append(HtmlListItem(Inserted('test')))
    item.internal.append(HtmlListItem(Subscript('test')))
    item.internal.append(HtmlListItem(Superscript('test')))
    item.internal.append(HtmlListItem(Emoji('emojicode')))
    doc.body.append(item)

    expected = []
    with open('tests/resources/document_simple_objects.html', 'r') as tf:
        for line in tf.readlines():
            expected.append(line[:-1])
    expected = "\n".join(expected)
    actual = doc.return_document
    assert actual == expected

def test_styles():
    doc = Document()
    div = Div()
    div.add_class('class1')
    div.add_class('class2')
    div.add_class('class3')
    doc.body.append(div)

    doc.styles.append({'class1': {'display': 'inline-block'}})
    doc.styles.append({'class2': [
        {'border-style': 'solid'},
    ]})
    doc.styles.append({'class3': [
        {'min-width': '300px'},
        {'max-width': '350px'},
    ]})
    expected = []
    with open('tests/resources/document_styles.html', 'r') as tf:
        for line in tf.readlines():
            expected.append(line)
    expected = "".join(expected)
    actual = doc.return_document
    assert actual == expected

def test_real_file():
    doc = Document()
    doc.body.append(Header(1, 'Example File'))
    doc.body.append(Header(2, 'Content header'))

    main_div = Div()
    color_list_1 = ['red', 'green', 'blue', 'purple', 'cyan']
    color_list_2 = ['lightcoral', 'cyan', 'red', 'green', 'purple']
    for index in range(5):
        div = Div()
        div.internal.append(f"Some content {index}")
        div.add_style(f'background-color: {color_list_1[index]};')
        div.add_style(f'color: {color_list_2[index]};')
        div.add_class('class1')
        div.add_class('class2')
        main_div.internal.append(div)
    doc.body.append(main_div)
    doc.styles.append({
        'class1': [{'border-style': 'solid'}],
        'class2': [
            {'display': 'inline-block'},
            {'min-width': '300px'},
            {'max-width': '350px'},
        ]
    })
    content = Paragraph()
    content.add_class('test1')
    content.add_style({'text-block': 'centered'})
    content.internal.append('simple string')
    content.internal.append(123)
    content.internal.append(Div())
    content.internal.append(Paragraph())
    content.internal.append(Link())
    content.internal.append(HyperLink())
    content.internal.append(Image())
    content.internal.append(Blockquote())
    content.internal.append(LineBreak())
    content.internal.append(Bold('test'))
    content.internal.append(Strong('test'))
    content.internal.append(Italic('test'))
    content.internal.append(Emphasized('test'))
    content.internal.append(Marked('test'))
    content.internal.append(Smaller('test'))
    content.internal.append(Deleted('test'))
    content.internal.append(Inserted('test'))
    content.internal.append(Subscript('test'))
    content.internal.append(Superscript('test'))
    content.internal.append(Emoji('emojicode'))
    doc.body.append(content)

    expected = []
    with open('tests/resources/document_actual_html_page.html', 'r') as tf:
        for line in tf.readlines():
            expected.append(line)
    expected = "".join(expected)
    actual = doc.return_document
    assert actual == expected
