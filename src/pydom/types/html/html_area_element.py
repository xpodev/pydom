from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLAreaElement(HTMLElementProps, total=False):
    alt: Optional[str]
    coords: Optional[str]
    download: Optional[str]
    href: Optional[str]
    href_lang: Optional[str]
    ping: Optional[str]
    referrer_policy: Optional[str]
    rel: Optional[str]
    shape: Optional[str]
    target: Optional[str]
