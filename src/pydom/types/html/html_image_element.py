from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLImageElement(HTMLElementProps, total=False):
    alt: Optional[str]
    cross_origin: Optional[str]
    decoding: Optional[str]
    height: Optional[str]
    importance: Optional[str]
    intrinsicsize: Optional[str]
    ismap: Optional[str]
    loading: Optional[str]
    referrer_policy: Optional[str]
    sizes: Optional[str]
    src: Optional[str]
    srcset: Optional[str]
    usemap: Optional[str]
    width: Optional[str]
