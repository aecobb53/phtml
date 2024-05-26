from phtml import Canvas
import pytest


def test_empty():
    item = Canvas()
    expected = [
        '<canvas></canvas>',
    ]
    actual = item.return_document
    assert actual == expected
