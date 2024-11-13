from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGUseElement
from ..types import ChildType


class Use(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGUseElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "use"
