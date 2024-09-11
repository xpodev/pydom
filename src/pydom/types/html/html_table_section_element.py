from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLTableSectionElement(HTMLElementProps, total=False):
    align: Optional[str]
    ch: Optional[str]
    choff: Optional[str]
    v_align: Optional[str]
