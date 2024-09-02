from typing import Literal
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLLinkElement(HTMLElementProps, total=False):
    html_as: str
    cross_origin: str
    disabled: str
    fetch_priority: Literal["high", "low", "auto"]
    href: str
    hreflang: str
    image_sizes: str
    integrity: str
    media: str
    referrer_policy: str
    rel: str
    sizes: str
    type: str
