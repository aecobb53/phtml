from phtml.classes.header import Header
from unittest import TestCase
import pytest


def test_empty():
    item = Header(1)
    expected = [
        '<h1>',
        '</h1>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = Header(2, 'HEADER')
    expected = [
        '<h2>',
        '    HEADER',
        '</h2>',
    ]
    actual = item.return_document
    assert actual == expected
