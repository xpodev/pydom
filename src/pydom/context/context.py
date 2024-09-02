from typing import (
    Callable,
    Any,
    TYPE_CHECKING,
    Dict,
    Tuple,
    TypeVar,
    Union,
    Optional,
    Type,
    List,
)

from typing_extensions import ParamSpec, TypeAlias, Concatenate

from ..utils.injector import Injector

if TYPE_CHECKING:
    from ..rendering.tree.nodes.context_node import ContextNode

T = TypeVar("T")
P = ParamSpec("P")

Feature: TypeAlias = Callable[Concatenate["Context", P], Any]

PropertyMatcher: TypeAlias = Union[Callable[Concatenate[str, Any, ...], bool], str]
PropertyTransformer: TypeAlias = Callable[
    Concatenate[str, Any, "ContextNode", ...], None
]

PostRenderTransformer: TypeAlias = Callable[Concatenate["ContextNode", ...], None]


class Context:
    def __init__(self) -> None:
        self.injector = Injector()
        self._prop_transformers: List[Tuple[PropertyMatcher, PropertyTransformer]] = []
        self._post_render_transformers: List[PostRenderTransformer] = []
        self._features: Dict[type, Any] = {}

    def add_feature(self, feature: Feature[P], *args: P.args, **kwargs: P.kwargs):
        result = feature(self, *args, **kwargs)
        if isinstance(feature, type):
            self._features[feature] = result

    def get_feature(self, feature: Type[T]) -> T:
        try:
            return self._features[feature]
        except KeyError:
            for cls in self._features:
                if issubclass(cls, feature):
                    return self._features[cls]

            raise

    def add_prop_transformer(
        self, matcher: PropertyMatcher, transformer: PropertyTransformer
    ):
        self._prop_transformers.append((matcher, self.inject(transformer)))

    def add_post_render_transformer(self, transformer: PostRenderTransformer):
        self._post_render_transformers.append(self.inject(transformer))

    @property
    def prop_transformers(self):
        return self._prop_transformers

    @property
    def post_render_transformers(self):
        return self._post_render_transformers

    def inject(self, callback: Callable) -> Callable:
        return self.injector.inject(callback)

    @classmethod
    def standard(cls) -> "Context":
        from .standard import add_standard_features

        context = cls()
        add_standard_features(context)
        return context


_DEFAULT_CONTEXT: Context


def get_context(context: Optional[Context] = None) -> Context:
    return context or _DEFAULT_CONTEXT


def set_default_context(context: Context) -> None:
    global _DEFAULT_CONTEXT
    _DEFAULT_CONTEXT = context
