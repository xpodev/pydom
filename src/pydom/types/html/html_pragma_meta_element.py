from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLPragmaMetaElement(HTMLElementProps, total=False):
    http_equiv: Optional[str]
