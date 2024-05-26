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
    item = Bold(internal='test')
    expected = '<b>test</b>'
    actual = item.return_content
    assert actual == expected

def test_Strong():
    item = Strong(internal='test')
    expected = '<strong>test</strong>'
    actual = item.return_content
    assert actual == expected

def test_Italic():
    item = Italic(internal='test')
    expected = '<i>test</i>'
    actual = item.return_content
    assert actual == expected

def test_Emphasized():
    item = Emphasized(internal='test')
    expected = '<em>test</em>'
    actual = item.return_content
    assert actual == expected

def test_Marked():
    item = Marked(internal='test')
    expected = '<mark>test</mark>'
    actual = item.return_content
    assert actual == expected

def test_Smaller():
    item = Smaller(internal='test')
    expected = '<small>test</small>'
    actual = item.return_content
    assert actual == expected

def test_Deleted():
    item = Deleted(internal='test')
    expected = '<del>test</del>'
    actual = item.return_content
    assert actual == expected

def test_Inserted():
    item = Inserted(internal='test')
    expected = '<ins>test</ins>'
    actual = item.return_content
    assert actual == expected

def test_Subscript():
    item = Subscript(internal='test')
    expected = '<sub>test</sub>'
    actual = item.return_content
    assert actual == expected

def test_Superscript():
    item = Superscript(internal='test')
    expected = '<sup>test</sup>'
    actual = item.return_content
    assert actual == expected

def test_Emoji():
    item = Emoji(internal='testcode')
    expected = 'testcode'
    actual = item.return_content
    assert actual == expected
