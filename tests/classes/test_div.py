from phtml import Div
from unittest import TestCase
import pytest


def test_empty():
    item = Div()
    expected = [
        '<div>',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Div()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<div class="testOne testTwo">',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Div()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<div style="testOne: testTwo;">',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_classes_and_styles():
    item = Div()
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<div class="testOne testTwo" style="testOne: testTwo;">',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_internal():
    item = Div()
    item.internal.append('test on the inside')
    expected = [
        '<div>',
        '    test on the inside',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_internal_object():
    item = Div()
    d1 = Div()
    d2 = Div()
    item.internal.extend([d1, d2])
    expected = [
        '<div>',
        '    <div>',
        '    </div>',
        '    <div>',
        '    </div>',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_added_internal_stuff():
    item = Div(internal='test_1')
    expected = [
        '<div>',
        '    test_1',
        '</div>',
    ]
    actual = item.return_document
    assert actual == expected

def test_return_string_version():
    item = Div(internal='test on the inside')
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = '<div class="testOne testTwo" style="testOne: testTwo;">test on the inside</div>'
    actual = item.return_string_version
    assert expected == actual
