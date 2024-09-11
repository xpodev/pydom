from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLMapElement(HTMLElementProps, total=False):
    name: Optional[str]
