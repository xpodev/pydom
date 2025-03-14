from typing import Dict, Generic, TypeVar, Union
from typing_extensions import Unpack
from ..types.styling.css_properties import CSSProperties


T = TypeVar("T")


class StyleSheet:
    class _StyleProperty(Generic[T]):
        def __init__(self, instance: "StyleSheet", name: str):
            self.instance = instance
            self.name = name.replace("_", "-")

        def __call__(self, value: T):
            self.instance.style[self.name] = value
            return self.instance

    def __init__(
        self,
        *styles: Union["StyleSheet", CSSProperties],
        **kwargs: Unpack[CSSProperties],
    ):
        self.style: Dict[str, object] = {}
        for style in styles:
            if isinstance(style, StyleSheet):
                style = style.style
            self.style.update(style)
        self.style.update(kwargs)
        self.style = {
            k.replace("_", "-"): v for k, v in self.style.items() if v is not None
        }

    def copy(self):
        return StyleSheet(self)

    def to_css(self):
        return "".join(map(lambda x: f"{x[0]}:{x[1]};", self.style.items()))

    def __str__(self):
        return self.to_css()

    def __getattr__(self, name: str):
        return StyleSheet._StyleProperty(self, name)
