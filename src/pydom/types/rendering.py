from typing import Collection, Literal, TYPE_CHECKING, Union
from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from ..component import Component
    from ..element import Element


Primitive: TypeAlias = Union[str, int, float, bool, None]
Renderable: TypeAlias = Union["Element", "Component"]

ChildType: TypeAlias = Union[Renderable, Primitive]
RenderResult: TypeAlias = Union[Renderable, Primitive]
ChildrenType: TypeAlias = Collection[ChildType]

RenderTarget: TypeAlias = Literal["json", "html"]

__all__ = [
    "ChildType",
    "ChildrenType",
    "Primitive",
    "Renderable",
    "RenderResult",
    "RenderTarget",
]
