from pydom import Component, Div
from pydom.element import Element

from .base import TestCase


class TestRender(TestCase):
    def test_render(self):
        self.assertRender(Div(), "<div></div>")

    def test_render_component(self):
        class MyComponent(Component):
            def render(self):
                return Div()

        self.assertRender(MyComponent(), "<div></div>")

    def test_render_element(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertRender(MyElement(), "<my-element></my-element>")

    def test_render_inline_element(self):
        class MyInlineElement(Element):
            tag_name = "my-element"
            inline = True

        self.assertRender(MyInlineElement(), "<my-element />")

    def test_render_nested(self):
        self.assertRender(Div(Div()), "<div><div></div></div>")

    def test_render_text(self):
        self.assertRender(Div("Hello"), "<div>Hello</div>")

    def test_render_attributes(self):
        self.assertRender(Div(id="my-id"), '<div id="my-id"></div>')

    def test_render_children(self):
        self.assertRender(Div(Div(), Div()), "<div><div></div><div></div></div>")

    def test_render_component_children(self):
        class MyComponent(Component):
            def render(self):
                return Div(Div(), Div())

        self.assertRender(MyComponent(), "<div><div></div><div></div></div>")

    def test_render_element_children(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertRender(
            MyElement(Div(), Div()),
            "<my-element><div></div><div></div></my-element>",
        )

    def test_render_text_children(self):
        self.assertRender(Div("Hello", "World"), "<div>HelloWorld</div>")

    def test_render_nested_children(self):
        self.assertRender(
            Div(Div(Div()), Div(Div())),
            "<div><div><div></div></div><div><div></div></div></div>",
        )

    def test_render_nested_text_children(self):
        self.assertRender(
            Div(Div("Hello"), Div("World")),
            "<div><div>Hello</div><div>World</div></div>",
        )

    def test_render_nested_mixed_children(self):
        self.assertRender(
            Div(Div("Hello", id="my-div"), Div(), "World"),
            '<div><div id="my-div">Hello</div><div></div>World</div>',
        )
