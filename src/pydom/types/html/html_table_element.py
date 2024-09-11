from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLTableElement(HTMLElementProps, total=False):
    border: Optional[str]
    cellpadding: Optional[str]
    cellspacing: Optional[str]
    frame: Optional[str]
    rules: Optional[str]
    summary: Optional[str]
    width: Optional[str]
