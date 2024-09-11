from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLAnchorElement(HTMLElementProps, total=False):
    download: Optional[str]
    href: Optional[str]
    href_lang: Optional[str]
    ping: Optional[str]
    referrer_policy: Optional[str]
    rel: Optional[str]
    target: Optional[str]
    type: Optional[str]
