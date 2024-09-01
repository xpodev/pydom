from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLPictureElement
from ..types import ChildType


class Picture(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLPictureElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "picture"
