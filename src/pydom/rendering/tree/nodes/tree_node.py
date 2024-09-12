from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
  from .element_node import ElementNode

class TreeNode:
    def __init__(self, *, parent: Optional["ElementNode"] = None):
        self.parent = parent