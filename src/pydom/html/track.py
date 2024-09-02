from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTrackElement
from ..types import ChildType


class Track(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTrackElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "track"
    inline = True
