from phtml import Comment
import pytest


def test_empty():
    item = Comment()
    expected = [
        '<!---->',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = Comment('CONTENT')
    expected = [
        '<!--',
        '    CONTENT',
        '-->',
    ]
    actual = item.return_document
    assert actual == expected
