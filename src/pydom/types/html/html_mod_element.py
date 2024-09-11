from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLModElement(HTMLElementProps, total=False):
    cite: Optional[str]
    datetime: str
