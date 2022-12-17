from phtml import Blockquote
from unittest import TestCase
import pytest


def test_empty():
    item = Blockquote()
    expected = [
        '<blockquote>',
        '</blockquote>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Blockquote()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<blockquote class="testOne testTwo">',
        '</blockquote>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Blockquote()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<blockquote style="testOne: testTwo;">',
        '</blockquote>',
    ]
    actual = item.return_document
    assert actual == expected

def test_classes_and_styles():
    item = Blockquote()
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<blockquote class="testOne testTwo" style="testOne: testTwo;">',
        '</blockquote>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_internal():
    item = Blockquote()
    item.internal.append('test on the inside')
    expected = [
        '<blockquote>',
        '    test on the inside',
        '</blockquote>',
    ]
    actual = item.return_document
    assert actual == expected

def test_internal_object():
    item = Blockquote()
    d1 = Blockquote()
    d2 = Blockquote()
    item.internal.extend([d1, d2])
    expected = [
        '<blockquote>',
        '    <blockquote>',
        '    </blockquote>',
        '    <blockquote>',
        '    </blockquote>',
        '</blockquote>',
    ]
    actual = item.return_document
    assert actual == expected
