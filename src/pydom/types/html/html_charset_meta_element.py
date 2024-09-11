from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLCharsetMetaElement(HTMLElementProps, total=False):
    charset: Optional[str]
