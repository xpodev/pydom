from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLListItemElement(HTMLElementProps, total=False):
    value: Optional[str]
