from phtml import Header
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

def test_content_class():
    item = Header(2, 'HEADER')
    item.add_class('test')
    expected = [
        '<h2 class="test">',
        '    HEADER',
        '</h2>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content_style():
    item = Header(2, 'HEADER')
    item.add_style({'test1': 'tester', 'test2': 'tester'})
    expected = [
        '<h2 style="test1: tester; test2: tester;">',
        '    HEADER',
        '</h2>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content_class_style():
    item = Header(2, 'HEADER')
    item.add_class('test')
    item.add_style({'test1': 'tester', 'test2': 'tester'})
    expected = [
        '<h2 class="test" style="test1: tester; test2: tester;">',
        '    HEADER',
        '</h2>',
    ]
    actual = item.return_document
    assert actual == expected
