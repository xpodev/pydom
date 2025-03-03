from string import ascii_letters
from uuid import uuid4
from typing_extensions import TypeGuard, overload, TypeVar, Iterator, Iterable

from ..types import Primitive


_T = TypeVar("_T")

ascii_length = len(ascii_letters)


def random_string(length=12):
    return "".join(
        ascii_letters[byte % ascii_length]
        for byte in b"".join(uuid4().bytes for _ in range(length // 16 + 1))
    )[:length]


# fmt: off
@overload
def to_iter(value: Iterable[_T]) -> Iterator[_T]: ...
@overload
def to_iter(value: _T) -> Iterator[_T]: ...

def to_iter(value):
    try:
        return iter(value)
    except TypeError:
        return iter((value,))
# fmt: on


def is_primitive(value) -> TypeGuard[Primitive]:
    return isinstance(value, (str, int, float, bool)) or value is None


def flatten(iterable):
    for item in iterable:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def remove_prefix(text: str, prefix: str) -> str:
    if hasattr(str, "removeprefix"):
        return text.removeprefix(prefix)
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text
