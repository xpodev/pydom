from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGForeignObjectElement
from ..types import ChildType


class ForeignObject(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGForeignObjectElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "foreignobject"
