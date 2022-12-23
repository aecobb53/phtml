from phtml import Style

def test_setup():
    item = Style(name='test', style_details={'color': 'green'})
    expected = ['test {color: green;}']
    actual = item.return_content
    assert actual == expected

def test_multiline():
    item = Style(name='test style div p', style_details={'color': 'green', 'background-color': 'blue'})
    expected = [
        'test style div p {',
        '    color: green;',
        '    background-color: blue;',
        '}',
    ]
    actual = item.return_content
    assert actual == expected

def test_singleline():
    item = Style(name='test style div p', style_details={'color': 'green', 'background-color': 'blue'})
    expected = 'test style div p {color: green; background-color: blue;}'
    actual = item.return_string_version
    assert actual == expected
