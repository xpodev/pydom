from typing import (
    Callable,
    Any,
    Dict,
    Tuple,
    TypeVar,
    Union,
    Optional,
    Type,
    List,
    overload,
)

from typing_extensions import ParamSpec, TypeAlias, Concatenate

from .transformers import (
    PostRenderTransformer,
    PostRenderTransformerFunction,
    PropertyTransformer,
    PropertyMatcherFunction,
    PropertyTransformerFunction,
)

from ..utils.injector import Injector

T = TypeVar("T")
P = ParamSpec("P")

Feature: TypeAlias = Callable[Concatenate["Context", P], Any]


class Context:
    def __init__(self) -> None:
        self.injector = Injector({Context: self})
        self._prop_transformers: List[
            Tuple[PropertyMatcherFunction, PropertyTransformerFunction]
        ] = []
        self._post_render_transformers: List[PostRenderTransformerFunction] = []
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

    @overload
    def add_prop_transformer(
        self,
        transformer: PropertyTransformer,
        /,
        *,
        before: Optional[List[Type[PropertyTransformer]]] = None,
        after: Optional[List[Type[PropertyTransformer]]] = None,
    ) -> None: ...
    @overload
    def add_prop_transformer(
        self,
        matcher: PropertyMatcherFunction,
        transformer: PropertyTransformerFunction,
        /,
        *,
        before: Optional[List[Type[PropertyTransformer]]] = None,
        after: Optional[List[Type[PropertyTransformer]]] = None,
    ) -> None: ...

    def add_prop_transformer(
        self,
        matcher: Union[PropertyMatcherFunction, PropertyTransformer],
        transformer: Optional[PropertyTransformerFunction] = None,
        /,
        *,
        before: Optional[List[Type[PropertyTransformer]]] = None,
        after: Optional[List[Type[PropertyTransformer]]] = None,
    ):
        if isinstance(matcher, PropertyTransformer):
            self._prop_transformers.append(
                (matcher.match, self.inject(matcher.transform))
            )
        else:
            assert transformer is not None
            self._prop_transformers.append((matcher, self.inject(transformer)))

    def add_post_render_transformer(
        self, transformer: Union[PostRenderTransformerFunction, PostRenderTransformer]
    ):
        if isinstance(transformer, PostRenderTransformer):
            self._post_render_transformers.append(self.inject(transformer.transform))
        else:
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
