from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLEmbedElement(HTMLElementProps, total=False):
    height: Optional[str]
    src: Optional[str]
    type: Optional[str]
    width: Optional[str]
