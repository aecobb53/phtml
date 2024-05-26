from phtml import IFrame
import pytest


def test_empty():
    item = IFrame()
    expected = [
        '<iframe></iframe>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = IFrame('CONTENT')
    expected = [
        '<iframe>',
        '    CONTENT',
        '</iframe>',
    ]
    actual = item.return_document
    assert actual == expected