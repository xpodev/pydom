from pydom import render, Div
from components import App, Page
from pydom.context.context import get_context
import pydom.context.standard.transformers as t

context = get_context()
context.add_prop_transformer(
    "class",
    lambda prop_name, prop_value, element: prop_value == "test",
    after=[t.ClassTransformer, t.StyleTransformer],
    before=[t.DashTransformer, t.InnerHTMLTransformer],
)

print("\n".join(map(str, context._prop_transformers)))
