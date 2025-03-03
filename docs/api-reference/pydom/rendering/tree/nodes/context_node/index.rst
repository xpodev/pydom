pydom.rendering.tree.nodes.context_node
=======================================

.. py:module:: pydom.rendering.tree.nodes.context_node


Classes
-------

.. autoapisummary::

   pydom.rendering.tree.nodes.context_node.ContextNode


Module Contents
---------------

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


