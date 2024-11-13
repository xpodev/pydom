from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEDisplacementMapElement
from ..types import ChildType


class FeDisplacementMap(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEDisplacementMapElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fedisplacementmap"
