from typing import Union
from ..types import Renderable, Primitive, RenderTarget


class RenderState:
    def __init__(
        self, *, root: Union[Renderable, Primitive], render_target: "RenderTarget", **kwargs
    ):
        self.root = root
        self.render_target: "RenderTarget" = render_target
        self.custom_data = kwargs
