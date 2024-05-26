from phtml import Span
import pytest


def test_empty():
    item = Span()
    expected = [
        '<span></span>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = Span('CONTENT')
    expected = [
        '<span>',
        '    CONTENT',
        '</span>',
    ]
    actual = item.return_document
    assert actual == expected
