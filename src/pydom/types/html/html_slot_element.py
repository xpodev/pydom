from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLSlotElement(HTMLElementProps, total=False):
    name: Optional[str]
