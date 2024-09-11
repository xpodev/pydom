from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLBaseElement(HTMLElementProps, total=False):
    href: Optional[str]
    target: Optional[str]
