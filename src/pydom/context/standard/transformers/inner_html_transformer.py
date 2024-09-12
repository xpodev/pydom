from pydom.rendering.tree.nodes import TextNode, ContextNode


def inner_html_transformer():
    def matcher(key, _):
        return key == "dangerously_set_inner_html"

    def transformer(_, inner_html, element: ContextNode):
        del element.props["dangerously_set_inner_html"]

        if element.children is None:
            return

        element.children.clear()
        element.children.append(TextNode(inner_html["__html"], parent=element.node))

    return matcher, transformer
