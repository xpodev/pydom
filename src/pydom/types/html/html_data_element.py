from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLDataElement(HTMLElementProps, total=False):
    value: Optional[str]
