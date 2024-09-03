from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLDataElement
from ..types import ChildType


class Data(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDataElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "data"
