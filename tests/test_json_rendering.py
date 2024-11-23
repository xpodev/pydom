from typing import Union, overload
from pydom import Component, Div
from pydom.element import Element
from pydom.types.rendering import Primitive, Renderable

from .base import TestCase


class TestRender(TestCase):
    @overload
    def assertRenderJson(
        self, component: Union[Renderable, Primitive], expected: dict, /, **kwargs
    ): ...
    @overload
    def assertRenderJson(
        self, component: Union[Renderable, Primitive], *, file: str, **kwargs
    ): ...

    def assertRenderJson(
        self,
        component: Union[Renderable, Primitive],
        expected=None,
        *,
        file=None,
        **kwargs,
    ):
        if expected is not None:
            self.assertRender(component, expected, to="json", **kwargs)
        elif file is not None:
            self.assertRender(component, file=file, to="json", **kwargs)
        else:
            raise ValueError("Expected or file must be provided")

    def test_render_json(self):
        self.assertRenderJson(Div(), {"type": "div", "children": [], "props": {}})

    def test_render_json_component(self):
        class MyComponent(Component):
            def render(self):
                return Div()

        self.assertRender(
            MyComponent(),
            {"type": "div", "children": [], "props": {}},
            to="json",
        )

    def test_render_json_element(self):
        class MyElement(Element):
            tag_name = "my-element"

        self.assertRenderJson(
            MyElement(),
            {"type": "my-element", "children": [], "props": {}},
        )

    def test_render_json_nested(self):
        self.assertRenderJson(
            Div(Div()),
            {
                "type": "div",
                "children": [{"type": "div", "children": [], "props": {}}],
                "props": {},
            },
        )

    def test_render_json_text(self):
        self.assertRenderJson(
            Div("Hello"),
            {"type": "div", "children": ["Hello"], "props": {}},
        )

    def test_render_json_attributes(self):
        self.assertRenderJson(
            Div(id="my-id"),
            {"type": "div", "children": [], "props": {"id": "my-id"}},
        )

    def test_render_json_nested_component(self):
        class MyComponent(Component):
            def render(self):
                return Div(
                    "Hello",
                    Div(),
                    id="my-id",
                    class_name="my-class",
                )

        class MyComponent2(Component):
            def render(self):
                return Div(
                    MyComponent(),
                    class_name="my-class",
                )

        self.assertRenderJson(
            MyComponent2(),
            {
                "type": "div",
                "children": [
                    {
                        "type": "div",
                        "children": [
                            "Hello",
                            {"type": "div", "children": [], "props": {}},
                        ],
                        "props": {"id": "my-id", "class": "my-class"},
                    }
                ],
                "props": {"class": "my-class"},
            },
        )
