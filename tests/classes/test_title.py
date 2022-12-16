from phtml.classes.title import Title
from unittest import TestCase
import pytest


def test_empty():
    item = Title()
    expected = [
        '<title>',
        '</title>',
    ]
    actual = item.return_document
    assert actual == expected

def test_not_empty():
    item = Title(content='TITLE')
    expected = [
        '<title>',
        '    TITLE',
        '</title>',
    ]
    actual = item.return_document
    assert actual == expected