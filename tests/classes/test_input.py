from phtml import Input
import pytest


def test_empty():
    item = Input()
    expected = [
        '<input>',
    ]
    actual = item.return_document
    assert actual == expected
