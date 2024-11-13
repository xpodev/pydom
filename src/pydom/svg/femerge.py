from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEMergeElement
from ..types import ChildType


class FeMerge(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEMergeElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "femerge"
