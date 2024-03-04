from phtml import Base
import pytest

def test_setup():
    item = Base()
    # assert item.classes == []
    # assert item.styles == []

def test_internal():
    item = Base(internal='test_one')
    expected = ['<None>    test_one']
    actual = item.return_document
    assert actual == expected

def test_return_not_none():
    item = Base().add_class('test_one')
    assert item != None

# class DivTest(TestCase):
#     def test_setup(self):
#         d = Div()
#         x=1
# def test_setup()

