from typing import Optional

from .tree_node import TreeNode


class ElementNode(TreeNode):
    def __init__(
        self,
        tag_name: str,
        props: Optional[dict] = None,
        children: Optional[list[TreeNode]] = None,
        parent: Optional["ElementNode"] = None,
    ):
        super().__init__(parent=parent)
        self.tag_name = tag_name
        self.props = dict(props or ())
        self.children = children