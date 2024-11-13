from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEMorphologyElement
from ..types import ChildType


class FeMorphology(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEMorphologyElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "femorphology"
