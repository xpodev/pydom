from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLProgressElement(HTMLElementProps, total=False):
    max: Optional[str]
    value: Optional[str]
