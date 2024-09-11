from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLOrderedListElement(HTMLElementProps, total=False):
    reversed: Optional[str]
    start: Optional[str]
