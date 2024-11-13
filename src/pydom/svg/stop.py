from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGStopElement
from ..types import ChildType


class Stop(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGStopElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "stop"
