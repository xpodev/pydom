from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLAudioElement(HTMLElementProps, total=False):
    auto_play: Optional[str]
    controls: Optional[str]
    loop: Optional[str]
    muted: Optional[str]
    preload: Optional[str]
    src: Optional[str]
