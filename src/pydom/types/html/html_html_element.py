from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLHtmlElement(HTMLElementProps, total=False):
    version: Optional[str]
    xmlns: Optional[str]
