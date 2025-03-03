pydom.rendering.tree.nodes
==========================

.. py:module:: pydom.rendering.tree.nodes


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/rendering/tree/nodes/context_node/index
   /api-reference/pydom/rendering/tree/nodes/element_node/index
   /api-reference/pydom/rendering/tree/nodes/text_node/index
   /api-reference/pydom/rendering/tree/nodes/tree_node/index


Classes
-------

.. autoapisummary::

   pydom.rendering.tree.nodes.ContextNode
   pydom.rendering.tree.nodes.ElementNode
   pydom.rendering.tree.nodes.TreeNode
   pydom.rendering.tree.nodes.TextNode


Package Contents
----------------

.. py:class:: ContextNode(node: pydom.rendering.tree.nodes.element_node.ElementNode, context: pydom.context.Context)

   .. py:attribute:: node


   .. py:attribute:: context


   .. py:method:: get_by_tag(tag: str)


   .. py:method:: get_all_by_tag(tag: str)


   .. py:method:: insert_after(node: Union[pydom.types.Renderable, pydom.types.Primitive])


   .. py:method:: insert_before(node: Union[pydom.types.Renderable, pydom.types.Primitive])


   .. py:method:: insert_child(index: int, node: Union[pydom.types.Renderable, pydom.types.Primitive])


   .. py:method:: append_child(node: Union[pydom.types.Renderable, pydom.types.Primitive])


   .. py:property:: children


   .. py:property:: parent


   .. py:property:: props


.. py:class:: ElementNode(tag_name: str, props: Optional[dict] = None, children: Optional[List[pydom.rendering.tree.nodes.tree_node.TreeNode]] = None, parent: Optional[ElementNode] = None)

   Bases: :py:obj:`pydom.rendering.tree.nodes.tree_node.TreeNode`


   .. py:attribute:: tag_name


   .. py:attribute:: props


   .. py:attribute:: children
      :value: None



.. py:class:: TreeNode(*, parent: Optional[pydom.rendering.tree.nodes.element_node.ElementNode] = None)

   .. py:attribute:: parent
      :value: None



.. py:class:: TextNode(text: str, *, parent: Optional[pydom.rendering.tree.nodes.element_node.ElementNode] = None)

   Bases: :py:obj:`pydom.rendering.tree.nodes.tree_node.TreeNode`


   .. py:attribute:: text


