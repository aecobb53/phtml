from phtml import Paragraph
import pytest


def test_empty():
    item = Paragraph()
    expected = [
        '<p></p>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_class():
    item = Paragraph()
    item.add_class(['testOne', 'testTwo'])
    expected = [
        '<p class="testOne testTwo"></p>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_styles():
    item = Paragraph()
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<p style="testOne: testTwo;"></p>',
    ]
    actual = item.return_document
    assert actual == expected

def test_classes_and_styles():
    item = Paragraph()
    item.add_class(['testOne', 'testTwo'])
    item.add_style({'testOne': 'testTwo'})
    expected = [
        '<p class="testOne testTwo" style="testOne: testTwo;"></p>',
    ]
    actual = item.return_document
    assert actual == expected

def test_simple_internal():
    item = Paragraph()
    item.internal.append('test on the inside')
    expected = [
        '<p>',
        '    test on the inside',
        '</p>',
    ]
    actual = item.return_document
    assert actual == expected
    
def test_internal_object():
    item = Paragraph()
    d1 = Paragraph()
    d2 = Paragraph()
    item.internal.extend([d1, d2])
    expected = [
        '<p>',
        '    <p></p>',
        '    <p></p>',
        '</p>',
    ]
    actual = item.return_document
    assert actual == expected
