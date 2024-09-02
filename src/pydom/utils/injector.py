from contextlib import contextmanager
from inspect import signature
from functools import wraps
from typing import Dict, Type, TypeVar, Union, overload, Callable

from typing_extensions import TypeAlias

T = TypeVar("T")

InjectFactory: TypeAlias = Callable[[], T]


class Injector:
    """
    A simple dependency injection container

    To get an instance of a class, you can use the `injector` property of the `Context` class.
    """

    def __init__(self):
        self.dependencies: Dict[type, Callable] = {}

    @overload
    def add(self, cls: Type[T], factory: Callable[[], T], /) -> None: ...
    @overload
    def add(self, cls: Type[T], instance: T, /) -> None: ...

    def add(self, cls: Type[T], dependency: Union[Callable[[], T], T], /) -> None:
        self.dependencies[cls] = (
            dependency if callable(dependency) else lambda: dependency
        )

    def inject(self, callback: Callable) -> Callable:
        @wraps(callback)
        def wrapper(*args, **kwargs):
            keyword_args = self.inject_params(callback)
            return callback(*args, **keyword_args, **kwargs)

        return wrapper

    def inject_params(self, callback: Callable):
        signature_ = signature(callback)
        parameters = signature_.parameters

        keyword_args = {}

        for name, parameter in parameters.items():
            if (
                parameter.kind
                in [parameter.POSITIONAL_OR_KEYWORD, parameter.KEYWORD_ONLY]
                and parameter.annotation in self.dependencies
            ):
                keyword_args[name] = self.dependencies[parameter.annotation]()

        return keyword_args

    @contextmanager
    def scope(self, dependencies: dict[type, InjectFactory]):
        original_dependencies = self.dependencies.copy()
        self.dependencies.update(dependencies)

        try:
            yield
        finally:
            self.dependencies = original_dependencies

""