from abc import abstractmethod, ABC
from typing import overload, Iterable, Tuple

from .types.rendering import RenderResult, ChildType


class Component(ABC):
    children: Tuple["ChildType", ...]

    @overload
    def __init__(self, *children: "ChildType") -> None: ...
    @overload
    def __init__(self, /, *, children: Iterable["ChildType"]) -> None: ...

    def __init__(self, *args, children=None) -> None:
        self.children = children if children is not None else args

    @abstractmethod
    def render(self, *_, **kwargs) -> "RenderResult": ...

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if cls.__init__ is Component.__init__:
            return

        original_init = cls.__init__

        def __init__(self, *args, children=None, **kwargs):
            Component.__init__(self, *(getattr(self, "children", children) or args))
            original_init(self, **kwargs)

        cls.__init__ = __init__

    def __call__(self, *children: "ChildType"):
        self.children = children
        return self
