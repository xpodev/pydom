from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLFormElement(HTMLElementProps, total=False):
    accept_charset: Optional[str]
    action: Optional[str]
    auto_complete: Optional[str]
    enctype: Optional[str]
    method: Optional[str]
    name: Optional[str]
    no_validate: Optional[str]
    target: Optional[str]
