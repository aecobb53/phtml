from phtml import Button
from unittest import TestCase
import pytest


def test_empty():
    item = Button()
    expected = [
        '<button>',
        '</button>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Button()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<button class="testOne testTwo">',
        '</button>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Button()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<button style="testOne: testTwo;">',
        '</button>',
    ]
    actual = item.return_document
    assert actual == expected

def test_classes_and_styles():
    item = Button()
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<button class="testOne testTwo" style="testOne: testTwo;">',
        '</button>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_internal():
    item = Button()
    item.internal.append('test on the inside')
    expected = [
        '<button>',
        '    test on the inside',
        '</button>',
    ]
    actual = item.return_document
    assert actual == expected
