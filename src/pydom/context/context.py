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

from typing_extensions import ParamSpec, TypeAlias, Concatenate, Self

from pydom.errors import Error

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
            Union[
                Tuple[PropertyMatcherFunction, PropertyTransformerFunction],
                PropertyTransformer,
            ]
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
        try:
            index = self._find_transformer_insertion_index(
                self._prop_transformers,
                before=before,
                after=after,
            )
        except Error as e:
            raise Error(
                str(e) + f"\nCould not add transformer {matcher} into prop_transformers"
            ) from e
        if isinstance(matcher, PropertyTransformer):
            self._prop_transformers.insert(index, matcher)

        else:
            assert transformer is not None
            self._prop_transformers.insert(index, (matcher, self.inject(transformer)))

    def add_post_render_transformer(
        self, transformer: Union[PostRenderTransformerFunction, PostRenderTransformer]
    ):
        try:
            index = self._find_transformer_insertion_index(
                self._post_render_transformers,
                before=[PostRenderTransformer],
                after=[PostRenderTransformer],
            )
        except Error as e:
            raise Error(
                str(e)
                + f"\nCould not add transformer {transformer} into post_render_transformers"
            ) from e

        if isinstance(transformer, PostRenderTransformer):
            self._post_render_transformers.insert(
                index, self.inject(transformer.transform)
            )
        else:
            self._post_render_transformers.insert(index, self.inject(transformer))

    @property
    def prop_transformers(self):
        return self._prop_transformers

    @property
    def post_render_transformers(self):
        return self._post_render_transformers

    def inject(self, callback: Callable) -> Callable:
        return self.injector.inject(callback)

    @classmethod
    def standard(cls) -> "Self":
        from .standard import add_standard_features

        context = cls()
        add_standard_features(context)
        return context

    def _find_transformer_insertion_index(
        self,
        transformer_list: List,
        before: Optional[List[Type]] = None,
        after: Optional[List[Type]] = None,
    ) -> int:
        if before is None and after is None:
            return len(transformer_list)

        transformer_list = [
            type(transformer)
            for transformer in transformer_list
            if isinstance(transformer, (PostRenderTransformer, PropertyTransformer))
        ]

        before_set = set(before) if before is not None else set()
        after_set = set(after) if after is not None else set()

        if not before_set.isdisjoint(after_set):
            raise Error(
                "Cannot specify the same transformer in both before and after lists"
            )

        before_indexes = {}
        after_indexes = {}
        for i, transformer in enumerate(transformer_list):
            if transformer in before_set:
                before_indexes[i] = transformer
            if transformer in after_set:
                after_indexes[i] = transformer

        min_before_index = min(before_indexes.keys(), default=-1)
        max_after_index = max(after_indexes.keys(), default=-1)

        if min_before_index == -1 and max_after_index == -1:
            return len(transformer_list)

        if min_before_index != -1 and max_after_index != -1:
            if min_before_index < max_after_index:
                raise Error(
                    f"Cannot insert transformer since {before_indexes[min_before_index].__name__}"
                    f" is before {after_indexes[max_after_index].__name__}"
                )

        return max_after_index + 1 if max_after_index != -1 else min_before_index


_DEFAULT_CONTEXT: Context


def get_context(context: Optional[Context] = None) -> Context:
    return context or _DEFAULT_CONTEXT


def set_default_context(context: Context) -> None:
    global _DEFAULT_CONTEXT
    _DEFAULT_CONTEXT = context
