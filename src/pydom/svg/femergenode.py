from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEMergeNodeElement
from ..types import ChildType


class FeMergeNode(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEMergeNodeElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "femergenode"
