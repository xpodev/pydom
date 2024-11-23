from pydom import render, Div, Script
from components import App, Page
from pydom.context.context import get_context
import pydom.context.standard.transformers as t
from utils import test_render_with_file

context = get_context()
context.add_prop_transformer(
    "class",
    lambda prop_name, prop_value, element: prop_value == "test",
    after=[t.ClassTransformer, t.StyleTransformer],
    before=[t.DashTransformer, t.InnerHTMLTransformer],
)

# print("\n".join(map(str, context._prop_transformers)))

s1 = Script(
    "console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }"
)
s2 = Script()(
    "console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }"
)
d1 = Div(
    "<script>console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }</script>"
)
d2 = Div()(
    "console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }"
)

# print(render(Div(s1)))
# print(render(Div(s2)))
# print(render(d1))
# print(render(d2))

print(
    test_render_with_file(
        Script(
            "console.log('hello world'); if (a < 2) { console.log('a is less than 2'); }"
        ),
        "html/test_escaping_script.html",
    )
)
