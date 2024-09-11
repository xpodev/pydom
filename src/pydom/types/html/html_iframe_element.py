from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLIFrameElement(HTMLElementProps, total=False):
    allow: Optional[str]
    allow_fullscreen: Optional[str]
    csp: Optional[str]
    frame_border: Optional[str]
    height: Optional[str]
    importance: Optional[str]
    loading: Optional[str]
    name: Optional[str]
    referrer_policy: Optional[str]
    sandbox: Optional[str]
    scrolling: Optional[str]
    seamless: Optional[str]
    src: Optional[str]
    srcdoc: Optional[str]
    width: Optional[str]
