from phtml import HyperLink
import pytest


def test_empty():
    item = HyperLink()
    expected = [
        '<link href="#">',
        '</link>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_href():
    item = HyperLink(href='example.com')
    expected = [
        '<link href="example.com">',
        '</link>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = HyperLink()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<link class="testOne testTwo" href="#">',
        '</link>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = HyperLink()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<link style="testOne: testTwo;" href="#">',
        '</link>',
    ]
    actual = item.return_document
    assert actual == expected

def test_href_classes_and_styles():
    item = HyperLink(href='example.com')
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<link class="testOne testTwo" style="testOne: testTwo;" href="example.com">',
        '</link>',
    ]
    actual = item.return_document
    assert actual == expected
