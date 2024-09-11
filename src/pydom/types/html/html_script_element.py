from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLScriptElement(HTMLElementProps, total=False):
    async_: Optional[bool]  # 'async' is a reserved keyword in Python, so using 'async_'
    cross_origin: Optional[str]
    defer: Optional[bool]
    integrity: Optional[str]
    nonce: Optional[str]
    referrer_policy: Optional[str]
    src: Optional[str]
    type: Optional[str]
