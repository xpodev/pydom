from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLTableCellElement(HTMLElementProps, total=False):
    abbr: Optional[str]
    colspan: Optional[str]
    headers: Optional[str]
    rowspan: Optional[str]
    scope: Optional[str]
