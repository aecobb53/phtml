from phtml import HtmlReader
import pytest

def test_setup():
    hr = HtmlReader()
    contents = hr.read_file(filepath='tests/resources/old_class_builds_for_manipulation.html')
    with open('testdoc_deleteme.html', 'w') as hf:
        hf.write(contents[0].return_document)
    x=1

def test_read_file():
    hr = HtmlReader()
    contents = hr.read_css_file(filepath='tests/resources/tiles.css')
    styles = []
    for style in contents:
        for line in style.return_content:
            styles.append(line)
        styles.append('')

    with open('testdoc_deleteme2.css', 'w') as cf:
        for line in styles:
            cf.write(line + '\n')

def test_specific_read_file():
    hr = HtmlReader()
    # contents = hr.read_file(filepath='tests/resources/deleteme_real_world_html.html')
    contents = hr.read_file(filepath='tests/resources/deleteme_real_world_html2.html')[0]

    path1 = 'deleteme.html'
    with open(path1, 'w') as hf:
        hf.write(contents.return_document)
    hr2 = HtmlReader()
    contents2 = hr2.read_file(path1)[0]

    
    path1 = 'deleteme2.html'
    with open(path1, 'w') as hf:
        hf.write(contents2.return_document)

        



    # styles = []
    # with open('deleteme_this_time.html', 'w') as hf:
    #     hf.write(contents[0].return_document)
    # x=1
    # for style in contents:
    #     for line in style.return_content:
    #         styles.append(line)
    #     styles.append('')

    # with open('testdoc_deleteme2.css', 'w') as cf:
    #     for line in styles:
    #         cf.write(line + '\n')
