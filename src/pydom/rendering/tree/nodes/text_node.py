from typing import TYPE_CHECKING, Optional

from .tree_node import TreeNode
from ....types import Primitive

if TYPE_CHECKING:
    from .element_node import ElementNode

class TextNode(TreeNode):
    def __init__(self, text: "Primitive", parent: Optional["ElementNode"] = None):
        super().__init__(parent=parent)
        self.text = str(text) if text is not None else ""
