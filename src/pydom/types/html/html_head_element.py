from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLHeadElement(HTMLElementProps, total=False):
    profile: Optional[str]
