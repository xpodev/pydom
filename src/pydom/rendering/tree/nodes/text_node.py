from html import escape
from typing import TYPE_CHECKING, Optional

from .tree_node import TreeNode

if TYPE_CHECKING:
    from .element_node import ElementNode

class TextNode(TreeNode):
    def __init__(self, text: str, *, parent: Optional["ElementNode"] = None):
        """
        Represents a text node in the DOM tree.

        Args:
            text (str): The text content of the node. **The text is not escaped**
            parent (ElementNode, optional): The parent element of the node. Defaults to None.
        """
        super().__init__(parent=parent)
        self.text = text
