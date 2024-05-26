# Python HyperText Markup Library - PHTML

- [Installation](iInstallation)
- [Document Object](#document-object)
- [Element Objects](#element-objects)
- [Parsing HTML](#parsing-html)
- [Finding Elements](#finding-elements)

---

# Installation

Installing using `pip`

```bash
pip install https://github.com/aecobb53/phtml
```

# Document Object

The primary phtml object is called a Document. This in reference to html documents. An understainding of HTML is very useful in understanding the lib.

Creating a Document:

```python
import phtml

doc = phtml.Document()
```

The Document is comprised of four parts and one attribute.

Parts:

- [head](#head)
- [body](#body)
- [styles](#styles)
- [scripts](#scripts)

Attributes:

- [indent](#indent) - This sets the indentation spaces when returning a multi-line document object

The Documents head and body can be populated with [Elements](#elements). Elements are explained later, but they can be added to the Document as seen below with `add_head_element` and `add_body_element` to add to the header and body tags respectivly. Think of Elements as tags in an HTML.

```python
header_element = phtml.Header(level=1, internal="I am an important note")
doc.add_body_element(obj=header_element)

header_element = phtml.Paragraph(internal="This is some content")
doc.add_body_element(obj=header_element)
```

You can return the HTML string of the results:

```python
html_details = doc.return_document
```

html_details is a string that looks like below:

```html
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <h1>
        I am an important note
    </h1>
    <p>
        This is some content
    </p>
</body>
</html>
```


# Components

## head

`Document.head` is a list of head elements for the HTML document. You can add to it with `<Document object>.add_head_element(<phtml Element>)`

## body

`Document.body` is a list of body elements for the HTML document. This is were your primary content is stored. You can add to it with `<Document object>.add_body_element(<phtml Element>)`

## styles

You can add style objects directly to an Element, to the Document itself, or load a styles file.

### Create Style object

```python
style_obj = Style()
style_obj = Style(style_details={'color': 'pink'})
content_list = style_obj.return_content
content_string = style_obj.return_string_version
```

`content_list`

```python
['{color: pink;}']
```

`content_string`

```python
'{color: pink;}'
```

---

```python
style_obj = Style(style_details={'color': 'pink', 'size': '60%'}, name='div a .example')
content_list = style_obj.return_content
content_string = style_obj.return_string_version
```

`content_list`

```python
[
    'div a .example {',
    '    color: pink;',
    '    size: 60%;',
    '}'
]
```

`content_string`

```python
'div a .example {color: pink; size: 60%;}'
```

### Adding a style to an Element:

```python
from phtml import Style, Div

element = Div()
element.add_style(style_obj='class1')

html_details = element.return_document
```

```html
<div style="color: pink;"></div>
```

### Adding a style to the Document itself

```python
from phtml import Document

doc = Document()
doc.add_style(style_obj='class1')

html_details = doc.return_document
```


### Loading a style file

## scripts

Im not great with JS or TS so this will be built out one day but it will be similar to the styles in that it can be applied to Elements directly or to the entire Document

## indent

When returning html, the lines are indented so you can set how indented they are.

## Elements

Elements are python classes of html tags. There are also string modifiers known as TextFormats.

Elements
TextFormats

## Object Nesting

As in html, you can imbed Elements in Elements. The function `add_element` appends the provided `obj` to the list of internal Elements.

```python
element = Div()
element.add_element(obj=Header(level=1, internal='Imbedded Header'))
```

## Returning Structure

`return_document` on the Document object returns the object as html.

`return_document` on any Element object instead returns a list of contents that make up the Element. You can get straight html with `return_string_version`. You can also get just the text with `text`.

## Parsing files

`HtmlReader` is used to read html, css, and eventually JS/TS files. 

functions:

- `read_file` - Parses an html file and returns a list of Document objects

- `read_css_file` - Parses a css file into styles that can be applied to a Document object

## Finding Elements

You can use `FindElement` to search for element types. Each search will return every Element that matches the search and all content within it. This can make nesting rather odd, but if you know what youre looking for, it works well.






TODO: 
- [X] Add classes
    - [X] Comment
    - [X] Form
    - [X] Table
- [X] If attribute value is None, reutrn just the key like button's autofocus
- [ ] Look into adding style references
    (descendant, child, adjacent, general)
- [X] Verify html_parser reads text_alterations like bold
- [X] Verify each class has the appropriate parameters in the init
- [X] Integrate scripts
    - [ ] Learn more about JS/TS
    - [X] Implement script adding







