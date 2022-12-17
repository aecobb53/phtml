from os import access
from phtml import *
# from phtml.classes.html_list import HtmlList, HtmlListItem
# from phtml.classes.div import Div
# from phtml.classes.paragraph import Paragraph
# from phtml.classes.link import Link
# from phtml.classes.image import Image
# from phtml.classes.blockquote import Blockquote
# from phtml.classes.html_list import HtmlList, HtmlListItem
# from phtml.classes.text_format import (
#     TextFormat,
#     LineBreak,
#     Bold,
#     Strong,
#     Italic,
#     Emphasized,
#     Marked,
#     Smaller,
#     Deleted,
#     Inserted,
#     Subscript,
#     Superscript,
#     Emoji,
# )
from unittest import TestCase
import pytest


def test_unordered_HtmlList_empty():
    item = HtmlList()
    expected = [
        '<ul>',
        '</ul>',
    ]
    actual = item.return_document
    assert actual == expected

def test_ordered_HtmlList_empty():
    item = HtmlList(ordered=True)
    expected = [
        '<ol>',
        '</ol>',
    ]
    actual = item.return_document
    assert actual == expected

def test_HtmlListItem_item_empty():
    item = HtmlListItem(content='test', list_item=True)
    expected = [
        '<li>test</li>'
    ]
    actual = item.return_document
    assert actual == expected

def test_HtmlListItem_list_description_empty():
    item = HtmlListItem(content='test', list_description=True)
    expected = [
        '<dl>test</dl>'
    ]
    actual = item.return_document
    assert actual == expected

def test_HtmlListItem_term_description_empty():
    item = HtmlListItem(content='test', term_description=True)
    expected = [
        '<dt>test</dt>'
    ]
    actual = item.return_document
    assert actual == expected

def test_HtmlListItem_term_in_description_list_empty():
    item = HtmlListItem(content='test', term_in_description_list=True)
    expected = [
        '<dd>test</dd>'
    ]
    actual = item.return_document
    assert actual == expected

def test_unordered_HtmlList_with_items():
    item = HtmlList()
    item.internal.append(HtmlListItem('one'))
    item.internal.extend([
        HtmlListItem('two'),
        HtmlListItem('three'),
        HtmlListItem(4),
    ])
    expected = [
        '<ul>',
        '    <li>one</li>',
        '    <li>two</li>',
        '    <li>three</li>',
        '    <li>4</li>',
        '</ul>'
    ]
    actual = item.return_document
    assert actual == expected

def test_List_with_ListItem():
    item = HtmlList()
    item.internal.append(HtmlListItem('string'))
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
    expected = [
        "<ul>",
        "    <li>string</li>",
        "    <li>123</li>",
        "    <li>",
        "        <div>",
        "        </div>",
        "    </li>",
        "    <li>",
        "        <p>",
        "        </p>",
        "    </li>",
        "    <li>",
        "        <a href=\"#\">",
        "        </a>",
        "    </li>",
        "    <li>",
        "        <img src=\"#\">",
        "    </li>",
        "    <li>",
        "        <blockquote>",
        "        </blockquote>",
        "    </li>",
        "    <li>",
        "        <b>test</b>",
        "    </li>",
        "    <li>",
        "        <strong>test</strong>",
        "    </li>",
        "    <li>",
        "        <i>test</i>",
        "    </li>",
        "    <li>",
        "        <em>test</em>",
        "    </li>",
        "    <li>",
        "        <mark>test</mark>",
        "    </li>",
        "    <li>",
        "        <small>test</small>",
        "    </li>",
        "    <li>",
        "        <del>test</del>",
        "    </li>",
        "    <li>",
        "        <ins>test</ins>",
        "    </li>",
        "    <li>",
        "        <sub>test</sub>",
        "    </li>",
        "    <li>",
        "        <sup>test</sup>",
        "    </li>",
        "    <li>",
        "        emojicode",
        "    </li>",
        "</ul>"
    ]
    actual = item.return_document
    assert actual == expected
