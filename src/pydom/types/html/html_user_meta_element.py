from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLUserMetaElement(HTMLElementProps, total=False):
    itemprop: Optional[str]
