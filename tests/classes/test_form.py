from phtml import Form, Textarea, Select, Option, Optiongroup, Fieldset, Label, Output
import pytest

def test_form_empty():
    item = Form()
    expected = [
        '<form></form>',
    ]
    actual = item.return_document
    assert actual == expected

def test_textarea_empty():
    item = Textarea()
    expected = [
        '<textarea></textarea>',
    ]
    actual = item.return_document
    assert actual == expected

def test_select_empty():
    item = Select()
    expected = [
        '<select></select>',
    ]
    actual = item.return_document
    assert actual == expected

def test_option_empty():
    item = Option()
    expected = [
        '<option></option>',
    ]
    actual = item.return_document
    assert actual == expected

def test_optiongroup_empty():
    item = Optiongroup()
    expected = [
        '<optgroup></optgroup>',
    ]
    actual = item.return_document
    assert actual == expected

def test_fieldset_empty():
    item = Fieldset()
    expected = [
        '<fieldset></fieldset>',
    ]
    actual = item.return_document
    assert actual == expected

def test_label_empty():
    item = Label()
    expected = [
        '<label></label>',
    ]
    actual = item.return_document
    assert actual == expected

def test_output_empty():
    item = Output()
    expected = [
        '<output></output>',
    ]
    actual = item.return_document
    assert actual == expected

