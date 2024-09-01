from typing import (
    Callable,
    Concatenate,
    ParamSpec,
    Any,
    TYPE_CHECKING,
    TypeVar,
    Union,
    Optional,
)

from ..utils.injector import Injector

if TYPE_CHECKING:
    from ..rendering.tree.nodes.context_node import ContextNode

T = TypeVar("T")

P = ParamSpec("P")
Feature = Callable[Concatenate["Context", P], Any]

PropertyMatcher = Union[Callable[Concatenate[str, Any, ...], bool], str]
PropertyTransformer = Callable[Concatenate[str, Any, "ContextNode", ...], None]
PostRenderTransformer = Callable[Concatenate["ContextNode", ...], None]


class Context:
    def __init__(self) -> None:
        self.injector = Injector()
        self._prop_transformers: list[tuple[PropertyMatcher, PropertyTransformer]] = []
        self._post_render_transformers: list[PostRenderTransformer] = []
        self._features: dict[type, Any] = {}

    def add_feature(self, feature: Feature[P], *args: P.args, **kwargs: P.kwargs):
        result = feature(self, *args, **kwargs)
        if isinstance(feature, type):
            self._features[feature] = result

    def get_feature(self, feature: type[T]) -> T:
        return self._features[feature]

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
