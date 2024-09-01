from typing_extensions import Unpack

from ..element import Element
from ..types.html import HTMLAudioElement
from ..types import ChildType


class Audio(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLAudioElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "audio"
