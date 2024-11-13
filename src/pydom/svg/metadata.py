from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGMetadataElement
from ..types import ChildType


class Metadata(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGMetadataElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "metadata"
