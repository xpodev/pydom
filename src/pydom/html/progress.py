from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLProgressElement
from ..types import ChildType


class Progress(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLProgressElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "progress"
