from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLSourceElement(HTMLElementProps, total=False):
    media: Optional[str]
    sizes: Optional[str]
    src: Optional[str]
    srcset: Optional[str]
    type: Optional[str]
