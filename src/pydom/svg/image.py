from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGImageElement
from ..types import ChildType


class Image(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGImageElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "image"
