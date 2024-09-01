from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLDataListElement
from ..types import ChildType


class DataList(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDataListElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "datalist"
