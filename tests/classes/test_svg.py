from phtml import Svg, SubParameter
import pytest


def test_svg_empty():
    item = Svg()
    expected = [
        '<svg></svg>',
    ]
    actual = item.return_document
    assert actual == expected

def test_subparameter_single_empty():
    item = SubParameter(start_tag='start-tag')
    expected = [
        '<start-tag>',
    ]
    actual = item.return_document
    assert actual == expected

def test_subparameter_both_empty():
    item = SubParameter(start_tag='start-tag', end_tag='end-tag')
    expected = [
        '<start-tag></end-tag>',
    ]
    actual = item.return_document
    assert actual == expected

def test_content():
    item = Svg('CONTENT')
    expected = [
        '<svg>',
        '    CONTENT',
        '</svg>',
    ]
    actual = item.return_document
    assert actual == expected
