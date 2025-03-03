import pydom as d
from pydom.context.context import get_context
from pydom.page import Page
from examples.htmx.utils.htmx_runtime import (
    HTMX,
    HTMXClassToolsExtension,
    HTMXExtension,
    HTMXSSEExtension,
    setup_htmx_transformers,
)

from ..base import TestCase

# HTMX Extensions to be registered
HTMX_EXTENSIONS: list[HTMXExtension] = [
    HTMXSSEExtension(),
    HTMXClassToolsExtension(),
]


class BasePage(Page):
    def head(self):
        yield HTMX().script()
        for ext in HTMX_EXTENSIONS:
            yield ext.script()


class TestRender(TestCase):
    def __init__(self, *args, **kwargs):
        context = get_context()
        setup_htmx_transformers(context, HTMX_EXTENSIONS)
        super().__init__(*args, **kwargs)

    def test_simple(self):
        self.assertRender(
            d.Div(hx_get="/some/route"), '<div hx-get="/some/route"></div>'
        )

    def test_hx_boost(self):
        self.assertRender(d.Div(hx_boost=True), "<div hx-boost></div>")
        self.assertRender(d.Div(hx_boost="true"), '<div hx-boost="true"></div>')
        self.assertRender(d.Div(hx_boost="false"), '<div hx-boost="false"></div>')

    def test_hx_on(self):
        self.assertRender(
            d.Div(hx_on_click="alert('hello')"),
            '<div hx-on:click="alert(&#x27;hello&#x27;)"></div>',
        )

    def test_hx_on_htmx(self):
        self.assertRender(
            d.Div(hx_on_htmx_before_request="alert('hello')"),
            '<div hx-on:htmx:before-request="alert(&#x27;hello&#x27;)"></div>',
        )

    def test_hx_on_htmx_short(self):
        self.assertRender(
            d.Div(hx_on__before_request="alert('hello')"),
            '<div hx-on::before-request="alert(&#x27;hello&#x27;)"></div>',
        )

    def test_sse_extension(self):
        self.assertRender(
            d.Div(hx_ext=HTMXSSEExtension.name)(d.Div(sse_connect="/sse")),
            '<div hx-ext="sse"><div hx-sse-connect="/sse"></div></div>',
        )

    def test_class_tools_extension(self):
        self.assertRender(
            d.Div(hx_ext=HTMXClassToolsExtension.name)(
                d.Div(hx_classes="add foo, remove foo:10s")
            ),
            '<div hx-ext="class-tools"><div classes="add foo, remove foo:10s"></div></div>',
        )
        self.assertRender(
            d.Div(hx_ext=HTMXClassToolsExtension.name)(
                d.Div(data_classes="add foo, remove foo:10s")
            ),
            '<div hx-ext="class-tools"><div data-classes="add foo, remove foo:10s"></div></div>',
        )
        self.assertRender(
            d.Div(hx_ext=HTMXClassToolsExtension.name)(
                d.Div(apply_parent_classes="add foo, remove foo:10s")
            ),
            '<div hx-ext="class-tools"><div apply-parent-classes="add foo, remove foo:10s"></div></div>',
        )
        self.assertRender(
            d.Div(hx_ext=HTMXClassToolsExtension.name)(
                d.Div(data_apply_parent_classes="add foo, remove foo:10s")
            ),
            '<div hx-ext="class-tools"><div data-apply-parent-classes="add foo, remove foo:10s"></div></div>',
        )
