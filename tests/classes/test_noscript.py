from phtml import Noscript
import pytest


def test_empty():
    item = Noscript()
    expected = [
        '<noscript></noscript>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = Noscript('CONTENT')
    expected = [
        '<noscript>',
        '    CONTENT',
        '</noscript>',
    ]
    actual = item.return_document
    assert actual == expected
