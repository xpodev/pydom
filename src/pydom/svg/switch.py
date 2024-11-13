from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGSwitchElement
from ..types import ChildType


class Switch(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGSwitchElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "switch"
