from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLIFrameElement
from ..types import ChildType


class IFrame(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLIFrameElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "iframe"
