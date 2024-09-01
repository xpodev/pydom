from ..context import Context
from .transformers import (
    class_transformer,
    dash_transformer,
    html_events_transformer,
    simple_transformer,
    style_transformer,
)


def add_standard_features(ctx: "Context"):
    ctx.add_prop_transformer(*class_transformer())
    ctx.add_prop_transformer(*simple_transformer())
    ctx.add_prop_transformer(*style_transformer())
    # Order matters
    ctx.add_prop_transformer(*html_events_transformer())
    ctx.add_prop_transformer(*dash_transformer())


__all__ = ["add_standard_features"]
