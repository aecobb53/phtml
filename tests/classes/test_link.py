from phtml import Link
from unittest import TestCase
import pytest


def test_empty():
    item = Link()
    expected = [
        '<a href="#">',
        '</a>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_href():
    item = Link(href='example.com')
    expected = [
        '<a href="example.com">',
        '</a>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Link()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<a class="testOne testTwo" href="#">',
        '</a>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Link()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<a style="testOne: testTwo;" href="#">',
        '</a>',
    ]
    actual = item.return_document
    assert actual == expected

def test_href_classes_and_styles():
    item = Link(href='example.com')
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<a class="testOne testTwo" style="testOne: testTwo;" href="example.com">',
        '</a>',
    ]
    actual = item.return_document
    assert actual == expected
