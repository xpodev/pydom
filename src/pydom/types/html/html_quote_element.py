from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLQuoteElement(HTMLElementProps, total=False):
    cite: Optional[str]
