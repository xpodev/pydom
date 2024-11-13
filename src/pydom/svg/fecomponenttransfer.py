from typing_extensions import Unpack

from ..element import Element
from ..types.svg import SVGFEComponentTransferElement
from ..types import ChildType


class FeComponentTransfer(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["SVGFEComponentTransferElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "fecomponenttransfer"
