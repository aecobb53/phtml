from phtml import (
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
import pytest


def test_LineBreak():
    item = LineBreak()
    expected = '<br>'
    actual = item.return_content
    assert actual == expected

def test_Bold():
    item = Bold(content='test')
    expected = '<b>test</b>'
    actual = item.return_content
    assert actual == expected

def test_Strong():
    item = Strong(content='test')
    expected = '<strong>test</strong>'
    actual = item.return_content
    assert actual == expected

def test_Italic():
    item = Italic(content='test')
    expected = '<i>test</i>'
    actual = item.return_content
    assert actual == expected

def test_Emphasized():
    item = Emphasized(content='test')
    expected = '<em>test</em>'
    actual = item.return_content
    assert actual == expected

def test_Marked():
    item = Marked(content='test')
    expected = '<mark>test</mark>'
    actual = item.return_content
    assert actual == expected

def test_Smaller():
    item = Smaller(content='test')
    expected = '<small>test</small>'
    actual = item.return_content
    assert actual == expected

def test_Deleted():
    item = Deleted(content='test')
    expected = '<del>test</del>'
    actual = item.return_content
    assert actual == expected

def test_Inserted():
    item = Inserted(content='test')
    expected = '<ins>test</ins>'
    actual = item.return_content
    assert actual == expected

def test_Subscript():
    item = Subscript(content='test')
    expected = '<sub>test</sub>'
    actual = item.return_content
    assert actual == expected

def test_Superscript():
    item = Superscript(content='test')
    expected = '<sup>test</sup>'
    actual = item.return_content
    assert actual == expected

def test_Emoji():
    item = Emoji(content='testcode')
    expected = 'testcode'
    actual = item.return_content
    assert actual == expected
