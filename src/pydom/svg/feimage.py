from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEImageElement
from ..types import ChildType


class FeImage(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEImageElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "feimage"
