from abc import ABC, abstractmethod
from typing import (
    Any,
    Callable,
    List,
    Optional,
    Type,
    Union,
    TYPE_CHECKING,
    Tuple,
)

from typing_extensions import ParamSpec, TypeAlias, Concatenate

if TYPE_CHECKING:
    from pydom.context import Context
    from pydom.rendering.tree.nodes import ContextNode


P = ParamSpec("P")

PropertyMatcherFunction: TypeAlias = Union[Callable[Concatenate[str, Any, P], bool], str]
PropertyTransformerFunction: TypeAlias = Callable[Concatenate[str, Any, "ContextNode", P], None]

if TYPE_CHECKING:

    class PropertyTransformer(ABC, Tuple[PropertyMatcherFunction, PropertyTransformerFunction]):
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


def property_transformer(
    matcher: Union[Callable[[str, Any], bool], str],
    *,
    context: Optional["Context"] = None,
    before: Optional[List[Type[PropertyTransformer]]] = None,
    after: Optional[List[Type[PropertyTransformer]]] = None,
):
    """
    A decorator to register a function as a property transformer.

    Args:
        matcher: A callable that takes a key and a value and returns a boolean
        indicating whether the transformer should be applied.
        If a string is provided, it is assumed to be a key that should be matched exactly.
        context: The context to register the transformer in. If not provided, the default context is used.

    Returns:
        A decorator that takes a transformer function and registers it.

    Example:
        >>> @property_transformer("class_name")
        ... def class_name_mapper(key, value, element):
        ...     if isinstance(class_name, list):
        ...         class_name = " ".join(class_name)
        ...
        ...     element.props["class"] = " ".join(str(class_name).split())

    """
    from ...context import get_context

    context = get_context(context)

    def decorator(func: PropertyTransformerFunction):
        context.add_prop_transformer(matcher, func, before=before, after=after)
        return func

    return decorator
