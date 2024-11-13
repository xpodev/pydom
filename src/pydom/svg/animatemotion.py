from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGAnimateMotionElement
from ..types import ChildType


class AnimateMotion(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGAnimateMotionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "animatemotion"
