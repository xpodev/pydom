from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLStyleElement(HTMLElementProps, total=False):
    media: Optional[str]
    nonce: Optional[str]
    scoped: Optional[str]
