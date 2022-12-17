from phtml import Image
from unittest import TestCase
import pytest


def test_empty():
    item = Image()
    expected = [
        '<img src="#">',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_src():
    item = Image()
    item.add_src('/images/favicon.ico')
    expected = [
        '<img src="/images/favicon.ico">',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Image()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<img class="testOne testTwo" src="#">',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Image()
    item.add_style(['testOne', 'testTwo'])
    expected = [
        '<img style="testOne testTwo" src="#">',
    ]
    actual = item.return_document
    assert actual == expected

def test_src_classes_and_styles():
    item = Image()
    item.add_src('/images/favicon.ico')
    item.add_class(['testOne', 'testTwo'])
    item.add_style(['testOne', 'testTwo'])
    expected = [
        '<img class="testOne testTwo" style="testOne testTwo" src="/images/favicon.ico">',
    ]
    actual = item.return_document
    assert actual == expected
