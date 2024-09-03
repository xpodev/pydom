from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLVideoElement
from ..types import ChildType


class Video(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLVideoElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "video"
