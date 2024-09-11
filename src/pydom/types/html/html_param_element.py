from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLParamElement(HTMLElementProps, total=False):
    name: Optional[str]
    value: Optional[str]
