pydom.rendering.tree
====================

.. py:module:: pydom.rendering.tree


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/rendering/tree/nodes/index
   /api-reference/pydom/rendering/tree/tree/index


Classes
-------

.. autoapisummary::

   pydom.rendering.tree.TreeNode
   pydom.rendering.tree.TextNode
   pydom.rendering.tree.ElementNode


Functions
---------

.. autoapisummary::

   pydom.rendering.tree.build_tree


Package Contents
----------------

.. py:function:: build_tree(renderable: Union[pydom.types.Renderable, pydom.types.Primitive], *, context: pydom.context.Context) -> pydom.rendering.tree.nodes.TreeNode

.. py:class:: TreeNode(*, parent: Optional[pydom.rendering.tree.nodes.element_node.ElementNode] = None)

   .. py:attribute:: parent
      :value: None



.. py:class:: TextNode(text: str, *, parent: Optional[pydom.rendering.tree.nodes.element_node.ElementNode] = None)

   Bases: :py:obj:`pydom.rendering.tree.nodes.tree_node.TreeNode`


   .. py:attribute:: text


.. py:class:: ElementNode(tag_name: str, props: Optional[dict] = None, children: Optional[List[pydom.rendering.tree.nodes.tree_node.TreeNode]] = None, parent: Optional[ElementNode] = None)

   Bases: :py:obj:`pydom.rendering.tree.nodes.tree_node.TreeNode`


   .. py:attribute:: tag_name


   .. py:attribute:: props


   .. py:attribute:: children
      :value: None



