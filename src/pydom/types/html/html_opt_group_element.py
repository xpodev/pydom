from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLOptGroupElement(HTMLElementProps, total=False):
    disabled: Optional[bool]
    label: Optional[str]
