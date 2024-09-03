from string import ascii_letters
from uuid import uuid4
from typing_extensions import TypeGuard

from ..types import Primitive

ascii_length = len(ascii_letters)


def random_string(length=12):
    return "".join(
        ascii_letters[byte % ascii_length]
        for byte in b"".join(uuid4().bytes for _ in range(length // 16 + 1))
    )[:length]


def to_iter(value):
    try:
        return iter(value)
    except TypeError:
        return iter((value,))


def is_primitive(value) -> TypeGuard[Primitive]:
    return isinstance(value, (str, int, float, bool)) or value is None
