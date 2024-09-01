from dataclasses import dataclass

try:
    from pydantic import BaseModel  # type: ignore
except ImportError:

    @dataclass
    class BaseModel: ...


__all__ = [
    "BaseModel",
]
