from phtml import Meta
import pytest


def test_empty():
    item = Meta()
    expected = [
        '<meta>',
    ]
    actual = item.return_document
    assert actual == expected
