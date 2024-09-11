from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLObjectElement(HTMLElementProps, total=False):
    data: Optional[str]
    form: Optional[str]
    height: Optional[str]
    name: Optional[str]
    type: Optional[str]
    usemap: Optional[str]
    width: Optional[str]
