from abc import ABC, abstractmethod
from typing import (
    Callable,
    Any,
    TYPE_CHECKING,
    Tuple,
    TypeVar,
    Union,
)

if TYPE_CHECKING:
    from pydom.rendering.tree.nodes import ContextNode


from typing_extensions import ParamSpec, TypeAlias, Concatenate

T = TypeVar("T")
P = ParamSpec("P")

PropertyMatcherFunction: TypeAlias = Union[
    Callable[Concatenate[str, Any, P], bool], str
]
PropertyTransformerFunction: TypeAlias = Callable[
    Concatenate[str, Any, "ContextNode", P], None
]

PostRenderTransformerFunction: TypeAlias = Callable[Concatenate["ContextNode", P], None]

if TYPE_CHECKING:

    class PropertyTransformer(
        ABC, Tuple[PropertyMatcherFunction, PropertyTransformerFunction]
    ):
        @abstractmethod
        def match(self, prop_name: str, prop_value, /) -> bool: ...
        @abstractmethod
        def transform(self, prop_name: str, prop_value, element: "ContextNode", /): ...

else:

    class PropertyTransformer(ABC):
        @abstractmethod
        def match(self, prop_name: str, prop_value, /) -> bool:
            pass

        @abstractmethod
        def transform(self, prop_name: str, prop_value, element: "ContextNode", /):
            pass

        def __iter__(self):
            return iter((self.match, self.transform))


class PostRenderTransformer(ABC):
    @abstractmethod
    def transform(self, element: "ContextNode"):
        pass
