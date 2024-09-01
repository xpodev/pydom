from abc import abstractmethod, ABC

from .types.rendering import RenderResult, ChildType


class Component(ABC):
    children: tuple["ChildType", ...]

    def __init__(self, *children: "ChildType") -> None:
        self.children = children

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
