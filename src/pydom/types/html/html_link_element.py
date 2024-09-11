from typing import Literal, Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLLinkElement(HTMLElementProps, total=False):
    html_as: Optional[str]
    cross_origin: Optional[str]
    disabled: Optional[str]
    fetch_priority: Optional[Literal["high", "low", "auto"]]
    href: Optional[str]
    hreflang: Optional[str]
    image_sizes: Optional[str]
    integrity: Optional[str]
    media: Optional[str]
    referrer_policy: Optional[str]
    rel: Optional[str]
    sizes: Optional[str]
    type: Optional[str]
