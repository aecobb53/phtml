from phtml import Script
import pytest


def test_empty():
    item = Script()
    expected = [
        '<script></script>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = Script(async_=True)
    expected = [
        '<script async></script>',
    ]
    actual = item.return_document
    assert actual == expected
