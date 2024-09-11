from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLFieldSetElement(HTMLElementProps, total=False):
    disabled: Optional[bool]
    form: Optional[str]
    name: Optional[str]
