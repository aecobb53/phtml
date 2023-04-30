from ..document import Document
# from phtml import Document
from ..classes import *
# from phtml.classes import *
from .parsers import parse_style


class MatchTag:
    def __init__(self):
        pass

    def match_tag(self, tag, tags_dict, content=None, current_element=None):
        element = None
        x=1
        if tag == 'html':
            element = Document(**tags_dict)
            current_element = element






        # from .blockquote import Blockquote
        elif tag == 'blockquote':
            element = Blockquote(**tags_dict)
        # from .blockquote import Inlinequote
        elif tag == 'inlinequote':
            element = Inlinequote(**tags_dict)
        # from .button import Button
        elif tag == 'button':
            element = Button(**tags_dict)
        # from .canvas import Canvas
        elif tag == 'canvas':
            element = Canvas(**tags_dict)
        # from .comment import Comment
        elif tag == '!--':
            element = Comment(**tags_dict)
        # from .datalist import Datalist
        elif tag == 'datalist':
            element = Datalist(**tags_dict)
        # from .div import Div
        elif tag == 'div':
            element = Div(**tags_dict)
        # from .fieldset import Fieldset
        elif tag == 'fieldset':
            element = Fieldset(**tags_dict)
        # from .fieldset import Legend
        elif tag == 'legend':
            element = Legend(**tags_dict)
        # from .form import Form
        elif tag == 'form':
            element = Form(**tags_dict)
        # from .header import Header
        elif tag.startswith('h') and len(tag) == 2:
            element = Header(level=tag[-1], **tags_dict)
        # from .html_list import HtmlList
        elif tag == 'ol':
            x=1
            element = HtmlList(ordered=True, **tags_dict)
        elif tag == 'ul':
            element = HtmlList(ordered=False, **tags_dict)
        # from .html_list import HtmlListItem
        elif tag == "li":
            x=1
            element = HtmlListItem(list_item=True, **tags_dict)
        elif tag == "ld":
            element = HtmlListItem(list_description=True, **tags_dict)
        elif tag == "td":
            element = HtmlListItem(term_description=True, **tags_dict)
        elif tag == "dd":
            element = HtmlListItem(term_in_description_list=True, **tags_dict)
        # from .hyper_link import HyperLink
        elif tag == 'link':
            element = HyperLink(**tags_dict)
        # from .iframe import IFrame
        elif tag == 'iframe':
            element = IFrame(**tags_dict)
        # from .image import Image
        elif tag == 'img':
            element = Image(**tags_dict)
        # from .input import Input
        elif tag == 'input':
            element = Input(**tags_dict)
        # from .label import Label
        elif tag == 'label':
            element = Label(**tags_dict)
        # from .link import Link
        elif tag == 'a':
            element = Link(**tags_dict)
        # from .meta import Meta
        elif tag == 'meta':
            element = Meta(**tags_dict)
        # from .noscript import Noscript
        elif tag == 'noscript':
            element = Noscript(**tags_dict)
        # from .option import Option
        elif tag == 'option':
            element = Option(**tags_dict)
        # from .output import Output
        elif tag == 'output':
            element = Output(**tags_dict)
        # from .paragraph import Paragraph
        elif tag == 'p':
            element = Paragraph(**tags_dict)
        # from .select import Select
        elif tag == 'select':
            element = Select(**tags_dict)
        # from .span import Span
        elif tag == 'span':
            element = Span(**tags_dict)
        # from .svg import Svg
        elif tag == 'svg':
            element = Svg(**tags_dict)
        # from .svg import SubParameter
        elif tag == 'subparameter':
            element = SubParameter(**tags_dict)
        # from .text_format import TextFormat
        elif tag == 'textformat':
            element = TextFormat(**tags_dict)
        # # from .text_format import LineBreak
        # elif tag == 'linebreak':
        #     element = LineBreak(**tags_dict)
        # # from .text_format import Bold
        # elif tag == 'bold':
        #     element = Bold(**tags_dict)
        # # from .text_format import Strong
        # elif tag == 'strong':
        #     element = Strong(**tags_dict)
        # # from .text_format import Italic
        # elif tag == 'italic':
        #     element = Italic(**tags_dict)
        # # from .text_format import Emphasized
        # elif tag == 'emphasized':
        #     element = Emphasized(**tags_dict)
        # # from .text_format import Marked
        # elif tag == 'marked':
        #     element = Marked(**tags_dict)
        # # from .text_format import Smaller
        # elif tag == 'smaller':
        #     element = Smaller(**tags_dict)
        # # from .text_format import Deleted
        # elif tag == 'deleted':
        #     element = Deleted(**tags_dict)
        # # from .text_format import Inserted
        # elif tag == 'inserted':
        #     element = Inserted(**tags_dict)
        # # from .text_format import Subscript
        # elif tag == 'subscript':
        #     element = Subscript(**tags_dict)
        # # from .text_format import Superscript
        # elif tag == 'superscript':
        #     element = Superscript(**tags_dict)
        # # from .text_format import Emoji
        # elif tag == 'emoji':
        #     element = Emoji(**tags_dict)
        elif tag == 'textarea':
            element = Textarea(**tags_dict)
        elif tag == 'title':
            element = Title(**tags_dict)







        # elif tag == 'div':
        #     element = Div(**tags_dict)
        # elif tag == 'p':
        #     element = Paragraph(**tags_dict)
        # elif tag.startswith('h') and len(tag) == 2:
        #     element = Header(level=tag[-1], **tags_dict)
        # elif tag == 'a':
        #     element = Link(**tags_dict)
        # elif tag == 'link':
        #     element = HyperLink(**tags_dict)
        # elif tag == 'img':
        #     element = Image(**tags_dict)
        # elif tag == 'title':
        #     element = Title(**tags_dict)
        # elif tag == 'button':
        #     element = Button(**tags_dict)
        # elif tag == 'span':
        #     element = Span(**tags_dict)
        # elif tag == 'meta':
        #     element = Meta(**tags_dict)
        # elif tag == 'input':
        #     element = Input(**tags_dict)
        # elif tag == 'svg':
        #     element = Svg(**tags_dict)
        # elif tag == 'canvas':
        #     element = Canvas(**tags_dict)
        # elif tag == 'iframe':
        #     element = IFrame(**tags_dict)
        # elif tag == 'noscript':
        #     element = Noscript(**tags_dict)
        # elif tag == 'form':
        #     element = Form(**tags_dict)
        # elif tag == 'label':
        #     element = Label(**tags_dict)
        # elif tag == 'select':
        #     element = Select(**tags_dict)
        # elif tag == 'option':
        #     element = Option(**tags_dict)
        # elif tag == 'textarea':
        #     element = Textarea(**tags_dict)
        # elif tag == 'legend':
        #     element = Legend(**tags_dict)
        # elif tag == 'datalist':
        #     element = Datalist(**tags_dict)
        # elif tag == 'output':
        #     element = Output(**tags_dict)
        # elif tag == '!--':
        #     element = Comment(**tags_dict)






        elif tag == 'style':
            element = content
            styles = parse_style(content)
            current_element.styles.extend(styles)
        else:
            if tag not in ['head', 'body']:
                x=1
                # raise TypeError(f'I am unsure what {tag} tag is')
        return element, current_element