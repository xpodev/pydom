from pydom.rendering.tree.nodes import TextNode

from ....rendering.transformers import PropertyTransformer


class InnerHTMLTransformer(PropertyTransformer):
    def match(self, prop_name: str, _) -> bool:
        return prop_name == "dangerously_set_inner_html"

    def transform(self, _, inner_html, element):
        del element.props["dangerously_set_inner_html"]

        if element.children is None:
            return

        element.children.clear()
        element.children.append(TextNode(inner_html["__html"], parent=element.node))
