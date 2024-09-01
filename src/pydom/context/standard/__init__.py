from ..context import Context
from .transformers.class_transformer import class_transformer
from .transformers.dash_transformer import dash_transformer
from .transformers.html_events_transformer import html_events_transformer
from .transformers.simple_transformer import simple_transformer
from .transformers.style_transformer import style_transformer


def add_standard_features(ctx: "Context"):
    ctx.add_prop_transformer(*class_transformer())
    ctx.add_prop_transformer(*simple_transformer())
    ctx.add_prop_transformer(*style_transformer())
    # Order matters
    ctx.add_prop_transformer(*html_events_transformer())
    ctx.add_prop_transformer(*dash_transformer())
