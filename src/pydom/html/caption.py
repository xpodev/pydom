from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTableCaptionElement
from ..types import ChildType


class Caption(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableCaptionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "caption"
