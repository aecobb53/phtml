from phtml import(
    Document,
    Div,
    Header,
    Button,
    Form,
    Input,
    Label,
    Select,
    Option,
    Textarea,
    Legend,
    Datalist,
    Output,
    HtmlReader,
)
from unittest import TestCase
import pytest


def test_create_html():
    doc = Document()
    div = Div().add_class('container')
    form = Form(method='GET').add_class('form-signing')

    header = Header(level=2, action='http://hamster.nax.lol:8200/').add_class('form-signin-heading')
    header.add_element('Please sign in')
    form.add_element(header)

    label = Label().add_class('checkbox')
    form.add_element(label)

    button = Button(type='submit').add_class('btn btn-lg btn-primary btn-block')
    button.add_element('Sign in')
    form.add_element(button)

    div.add_element(form)
    doc.add_body_element(div)
    x=1
    with open('tests/resources/document_form2.html', 'w') as tf:
        tf.write(doc.return_document)

    x=1

    hr = HtmlReader()
    details = hr.read_file('tests/resources/document_form.html')

    x=1

    with open('tests/resources/document_form3.html', 'w') as tf:
        tf.write(details.return_document)

    x=1


