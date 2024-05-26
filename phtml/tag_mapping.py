

class TagMapping:
    mapping_ = {
        "blockquote": {
            "file": "blockquote",
            "class": "Blockquote",
            "tag_start": "blockquote",
            "tag_end": "blockquote"
        },
        "q": {
            "file": "blockquote",
            "class": "Inlinequote",
            "tag_start": "q",
            "tag_end": "q"
        },
        "body": {
            "file": "body",
            "class": "Body",
            "tag_start": "body",
            "tag_end": "body"
        },
        "button": {
            "file": "button",
            "class": "Button",
            "tag_start": "button",
            "tag_end": "button"
        },
        "canvas": {
            "file": "canvas",
            "class": "Canvas",
            "tag_start": "canvas",
            "tag_end": "canvas"
        },
        "!--": {
            "file": "comment",
            "class": "Comment",
            "tag_start": "!--",
            "tag_end": "--"
        },
        "div": {
            "file": "div",
            "class": "Div",
            "tag_start": "div",
            "tag_end": "div"
        },
        "form": {
            "file": "form",
            "class": "Form",
            "tag_start": "form",
            "tag_end": "form"
        },
        "head": {
            "file": "head",
            "class": "Head",
            "tag_start": "head",
            "tag_end": "head"
        },
        "html": {
            "file": "html",
            "class": "Html",
            "tag_start": "html",
            "tag_end": "html"
        },
        "textarea": {
            "file": "form",
            "class": "Textarea",
            "tag_start": "textarea",
            "tag_end": "textarea"
        },
        "select": {
            "file": "form",
            "class": "Select",
            "tag_start": "select",
            "tag_end": "select"
        },
        "option": {
            "file": "form",
            "class": "Option",
            "tag_start": "option",
            "tag_end": "option"
        },
        "optgroup": {
            "file": "form",
            "class": "Optiongroup",
            "tag_start": "optgroup",
            "tag_end": "optgroup"
        },
        "fieldset": {
            "file": "form",
            "class": "Fieldset",
            "tag_start": "fieldset",
            "tag_end": "fieldset"
        },
        "label": {
            "file": "form",
            "class": "Label",
            "tag_start": "label",
            "tag_end": "label"
        },
        "output": {
            "file": "form",
            "class": "Output",
            "tag_start": "output",
            "tag_end": "output"
        },
        "h1": {
            "file": "header",
            "class": "Header",
            "tag_start": "h1",
            "tag_end": "h1"
        },
        "h2": {
            "file": "header",
            "class": "Header",
            "tag_start": "h2",
            "tag_end": "h2"
        },
        "h3": {
            "file": "header",
            "class": "Header",
            "tag_start": "h3",
            "tag_end": "h3"
        },
        "h4": {
            "file": "header",
            "class": "Header",
            "tag_start": "h4",
            "tag_end": "h4"
        },
        "h5": {
            "file": "header",
            "class": "Header",
            "tag_start": "h5",
            "tag_end": "h5"
        },
        "h6": {
            "file": "header",
            "class": "Header",
            "tag_start": "h6",
            "tag_end": "h6"
        },
        "ol": {
            "file": "html_list",
            "class": "HtmlList",
            "tag_start": "ol",
            "tag_end": "ol"
        },
        "ul": {
            "file": "html_list",
            "class": "HtmlList",
            "tag_start": "ul",
            "tag_end": "ul"
        },
        "li": {
            "file": "html_list",
            "class": "HtmlListItem",
            "tag_start": "li",
            "tag_end": "li"
        },
        "dl": {
            "file": "html_list",
            "class": "HtmlListItem",
            "tag_start": "dl",
            "tag_end": "dl"
        },
        "dt": {
            "file": "html_list",
            "class": "HtmlListItem",
            "tag_start": "dt",
            "tag_end": "dt"
        },
        "dd": {
            "file": "html_list",
            "class": "HtmlListItem",
            "tag_start": "dd",
            "tag_end": "dd"
        },
        # "link": {
        #     "file": "hyper_link",
        #     "class": "HyperLink",
        #     "tag_start": "link",
        #     "tag_end": "link"
        # },
        "iframe": {
            "file": "iframe",
            "class": "IFrame",
            "tag_start": "iframe",
            "tag_end": "iframe"
        },
        "img": {
            "file": "image",
            "class": "Image",
            "tag_start": "img",
            "tag_end": None
        },
        "input": {
            "file": "input",
            "class": "Input",
            "tag_start": "input",
            "tag_end": None
        },
        "a": {
            "file": "link",
            "class": "Link",
            "tag_start": "a",
            "tag_end": "a"
        },
        "meta": {
            "file": "meta",
            "class": "Meta",
            "tag_start": "meta",
            "tag_end": None
        },
        "noscript": {
            "file": "noscript",
            "class": "Noscript",
            "tag_start": "noscript",
            "tag_end": "noscript"
        },
        "p": {
            "file": "paragraph",
            "class": "Paragraph",
            "tag_start": "p",
            "tag_end": "p"
        },
        "script": {
            "file": "script",
            "class": "Script",
            "tag_start": "script",
            "tag_end": "script"
        },
        "span": {
            "file": "span",
            "class": "Span",
            "tag_start": "span",
            "tag_end": "span"
        },
        "svg": {
            "file": "svg",
            "class": "Svg",
            "tag_start": "svg",
            "tag_end": "svg"
        },
        "None": {
            "file": "text_format",
            "class": "TextFormat",
            "tag_start": None,
            "tag_end": None
        },
        "table": {
            "file": "table",
            "class": "Table",
            "tag_start": "table",
            "tag_end": "table"
        },
        "tr": {
            "file": "table",
            "class": "TableRow",
            "tag_start": "tr",
            "tag_end": "tr"
        },
        "th": {
            "file": "table",
            "class": "TableHeader",
            "tag_start": "th",
            "tag_end": "th"
        },
        "td": {
            "file": "table",
            "class": "TableData",
            "tag_start": "td",
            "tag_end": "td"
        },
        "br": {
            "file": "text_format",
            "class": "LineBreak",
            "tag_start": "br",
            "tag_end": None
        },
        "b": {
            "file": "text_format",
            "class": "Bold",
            "tag_start": "b",
            "tag_end": "b"
        },
        "strong": {
            "file": "text_format",
            "class": "Strong",
            "tag_start": "strong",
            "tag_end": "strong"
        },
        "i": {
            "file": "text_format",
            "class": "Italic",
            "tag_start": "i",
            "tag_end": "i"
        },
        "em": {
            "file": "text_format",
            "class": "Emphasized",
            "tag_start": "em",
            "tag_end": "em"
        },
        "mark": {
            "file": "text_format",
            "class": "Marked",
            "tag_start": "mark",
            "tag_end": "mark"
        },
        "small": {
            "file": "text_format",
            "class": "Smaller",
            "tag_start": "small",
            "tag_end": "small"
        },
        "del": {
            "file": "text_format",
            "class": "Deleted",
            "tag_start": "del",
            "tag_end": "del"
        },
        "ins": {
            "file": "text_format",
            "class": "Inserted",
            "tag_start": "ins",
            "tag_end": "ins"
        },
        "sub": {
            "file": "text_format",
            "class": "Subscript",
            "tag_start": "sub",
            "tag_end": "sub"
        },
        "sup": {
            "file": "text_format",
            "class": "Superscript",
            "tag_start": "sup",
            "tag_end": "sup"
        },
        "title": {
            "file": "title",
            "class": "Title",
            "tag_start": "title",
            "tag_end": "title"
        }
    }

    def from_tag(self, tag: str):
        return self.mapping_[tag]

    def from_file(self, filename: str):
        for item in self.mapping_.values():
            if item["file"] == filename:
                return item

    def from_class(self, classname: str):
        for item in self.mapping_.values():
            if item["class"] == classname:
                return item
