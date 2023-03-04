import re

from .html_reader import HtmlReader
from .document import Document
from .classes.base import Base
from .classes.text_format import TextFormat
from .classes import *


class FindElement:
    def __init__(self):
        self.html_content = []

    def read_file(self, path):
        hr = HtmlReader()
        self.html_content = hr.read_file(filepath=path)[0]
        return self.html_content

    def find_elements(self, obj, element_type, **kwargs):
        for key in list(kwargs.keys()):
            value = kwargs[key]
            if key.startswith('_'):
                kwargs[key[1:]] = value
                del kwargs[key]
        elements = self._generate_element_list(obj=obj)
        if not isinstance(element_type, (list, tuple, set)):
            element_type = [element_type]
        element_types = tuple(element_type)
        results = []
        for el in elements:
            if isinstance(el, element_types):
                for key, value in kwargs.items():
                    if key in el.attributes:
                        attr_val = el.attributes[key]
                        if isinstance(attr_val, (list, tuple, set, dict)):
                            if any([re.search(value, av) for av in attr_val]):
                                results.append(el)
                        else:
                            if re.search(value, attr_val):
                                results.append(el)
        return results

    def _generate_element_list(self, obj):
        elements = []
        if isinstance(obj, Document):
            for obj_iter in obj.head:
                sub_element_list = self._generate_element_list(obj=obj_iter)
                elements.extend(sub_element_list)
            for obj_iter in obj.body:
                sub_element_list = self._generate_element_list(obj=obj_iter)
                elements.extend(sub_element_list)
        elif isinstance(obj, Base):
            elements.append(obj)
            for obj_iter in obj.internal:
                sub_element_list = self._generate_element_list(obj=obj_iter)
                elements.extend(sub_element_list)
        else:
            elements = [obj]
        return elements

