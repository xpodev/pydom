from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGStyleElement
from ..types import ChildType


class Style(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGStyleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "style"
