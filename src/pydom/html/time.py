from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLTimeElement
from ..types import ChildType


class Time(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTimeElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "time"
