from phtml import HtmlReader
import pytest

def test_setup():
    hr = HtmlReader()
    contents = hr.read_file('tests/resources/old_class_builds_for_manipulation.html')
    with open('testdoc_deleteme.html', 'w') as hf:
        hf.write(contents[0].return_document)
    x=1
