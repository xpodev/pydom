from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLSelectElement
from ..types import ChildType


class Select(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLSelectElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "select"
