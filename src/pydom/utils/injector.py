from contextlib import contextmanager
from inspect import signature, iscoroutinefunction
from functools import wraps
from typing import Any, Dict, Optional, Type, TypeVar, Union, overload, Callable

from typing_extensions import TypeAlias

T = TypeVar("T")

InjectFactory: TypeAlias = Callable[[], T]


class Injector:
    """
    A simple dependency injection container

    To get an instance of a class, you can use the `injector` property of the `Context` class.
    """

    def __init__(self, defaults: Optional[Dict[type, Any]] = None):
        self.dependencies: Dict[type, Callable] = {}
        if defaults:
            for cls, dependency in defaults.items():
                self.add(cls, dependency)

    @overload
    def add(self, cls: Type[T], factory: InjectFactory, /) -> None: ...
    @overload
    def add(self, cls: Type[T], instance: T, /) -> None: ...

    def add(self, cls: Type[T], dependency: Union[InjectFactory, T], /) -> None:
        self.dependencies[cls] = (
            dependency if callable(dependency) else lambda: dependency
        )

    def inject(self, callback: Callable) -> Callable:
        if iscoroutinefunction(callback):

            @wraps(callback)
            async def wrapper(*args, **kwargs):  # type: ignore
                keyword_args = self.inject_params(callback)
                return await callback(*args, **keyword_args, **kwargs)

        else:

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
    def scope(self, dependencies: Dict[type, InjectFactory]):
        original_dependencies = self.dependencies.copy()
        self.dependencies.update(dependencies)

        try:
            yield
        finally:
            self.dependencies = original_dependencies
