from typing import Optional, Literal
from pydom.types.svg.svg_element_props import SVGElementProps


class SVGAnchorElement(SVGElementProps, total=False):
    download: Optional[str]
    href: Optional[str]
    href_lang: Optional[str]
    ping: Optional[str]
    referrer_policy: Optional[
        Literal[
            "no-referrer",
            "no-referrer-when-downgrade",
            "origin",
            "origin-when-cross-origin",
            "same-origin",
            "strict-origin",
            "strict-origin-when-cross-origin",
            "unsafe-url",
        ]
    ]
    rel: Optional[str]
    system_language: Optional[str]
    target: Optional[Literal["_blank", "_self", "_parent", "_top"]]
    type: Optional[str]
