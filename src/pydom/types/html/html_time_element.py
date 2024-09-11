from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLTimeElement(HTMLElementProps, total=False):
    datetime: Optional[str]
