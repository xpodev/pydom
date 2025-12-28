from ..context import Context
from . import transformers as t


def add_standard_features(ctx: Context):
    ctx.add_prop_transformer(t.FalsyTransformer())
    ctx.add_prop_transformer(t.ClassTransformer())
    ctx.add_prop_transformer(t.SimpleTransformer())
    ctx.add_prop_transformer(t.SimpleInputTransformer())
    ctx.add_prop_transformer(t.StyleTransformer())
    ctx.add_prop_transformer(t.InnerHTMLTransformer())
    # Order matters
    ctx.add_prop_transformer(t.HTMLEventsTransformer())
    ctx.add_prop_transformer(t.DashTransformer())


__all__ = ["add_standard_features"]
