from typing import Optional
from pydom.types.html.html_element_props import HTMLElementProps


class HTMLTrackElement(HTMLElementProps, total=False):
    default: Optional[str]
    kind: Optional[str]
    label: Optional[str]
    src: Optional[str]
    srclang: Optional[str]
