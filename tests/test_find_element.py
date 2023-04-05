from phtml import FindElement
from phtml import *
import pytest

def test_find_element():
    fe = FindElement()
    content = fe.read_file(path='tests/resources/real_world_html.html')
    elements = fe.find_elements(obj=content, element_type=Div, _class='^athlete-basic-line$')
    for el in elements:
        a = el.text
    x=1
