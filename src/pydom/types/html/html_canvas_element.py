from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLCanvasElement(HTMLElementProps, total=False):
    height: Optional[str]
    width: Optional[str]
