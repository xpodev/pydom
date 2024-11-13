from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEFloodElement
from ..types import ChildType


class FeFlood(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEFloodElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "feflood"
