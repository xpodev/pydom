from typing import Collection, Literal, TypeAlias, TYPE_CHECKING, Union

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
