from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLOptionElement(HTMLElementProps, total=False):
    disabled: Optional[bool]
    label: Optional[str]
    selected: Optional[bool]
    value: Optional[str]
