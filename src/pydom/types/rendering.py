from typing import Collection, Dict, List, Literal, TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypedDict

if TYPE_CHECKING:
    from ..component import Component
    from ..element import Element


Primitive: TypeAlias = Union[str, int, float, bool, None]
Renderable: TypeAlias = Union["Element", "Component"]

ChildType: TypeAlias = Union[Union[Renderable, Primitive], Collection[Union[Renderable, Primitive]]]
RenderResult: TypeAlias = Union[Renderable, Primitive]
ChildrenType: TypeAlias = Collection[ChildType]

RenderTarget: TypeAlias = Literal["json", "html"]


class RenderResultJSON(TypedDict, total=False, closed=True):
    type: str
    props: Dict[str, Primitive]
    children: List["RenderResultJSON"]


__all__ = [
    "ChildType",
    "ChildrenType",
    "Primitive",
    "Renderable",
    "RenderResult",
    "RenderTarget",
    "RenderResultJSON",
]
