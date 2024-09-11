from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLVideoElement(HTMLElementProps, total=False):
    auto_play: Optional[str]
    controls: Optional[str]
    cross_origin: Optional[str]
    height: Optional[str]
    loop: Optional[str]
    muted: Optional[str]
    plays_inline: Optional[str]
    poster: Optional[str]
    preload: Optional[str]
    src: Optional[str]
    width: Optional[str]
