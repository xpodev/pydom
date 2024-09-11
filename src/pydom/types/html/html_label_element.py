from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLLabelElement(HTMLElementProps, total=False):
    html_for: Optional[str]
