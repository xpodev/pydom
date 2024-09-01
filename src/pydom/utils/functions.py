from string import ascii_letters
from uuid import uuid4
from typing_extensions import TypeGuard

from ..types import Primitive

ascii_length = len(ascii_letters)


def short_uuid(length=12):
    original_uuid = uuid4()
    hex_string = original_uuid.hex
    base62_uuid = ""
    for i in range(0, len(hex_string), 2):
        hex_byte = int(hex_string[i : i + 2], 16)
        base62_uuid += ascii_letters[hex_byte % ascii_length]

    short_uuid = base62_uuid[:length]

    return short_uuid


def to_iter(value):
    try:
        return iter(value)
    except TypeError:
        return iter((value,))


def is_primitive(value) -> TypeGuard[Primitive]:
    return isinstance(value, (str, int, float, bool)) or value is None
