from ..context import Context
from . import transformers as t


def add_standard_features(ctx: "Context"):
    ctx.add_prop_transformer(*t.falsy_transformer())
    ctx.add_prop_transformer(*t.class_transformer())
    ctx.add_prop_transformer(*t.simple_transformer())
    ctx.add_prop_transformer(*t.style_transformer())
    ctx.add_prop_transformer(*t.inner_html_transformer())
    # Order matters
    ctx.add_prop_transformer(*t.html_events_transformer())
    ctx.add_prop_transformer(*t.dash_transformer())


__all__ = ["add_standard_features"]
