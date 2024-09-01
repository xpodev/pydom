from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLMapElement
from ..types import ChildType


class Map(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLMapElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "map"
