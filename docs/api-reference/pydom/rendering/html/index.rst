pydom.rendering.html
====================

.. py:module:: pydom.rendering.html


Functions
---------

.. autoapisummary::

   pydom.rendering.html.render_html


Module Contents
---------------

.. py:function:: render_html(element: pydom.types.RenderResult, *, context: Optional[pydom.context.Context] = None, pretty=False, tab_indent=1, **render_state_data) -> str

   Renders the given element into an HTML string.

   Args:
       element (Renderable | Primitive): The element to be rendered.
       pretty (bool, optional): Whether to format the HTML string with indentation and line breaks. Defaults to False.
       tab_indent (int, optional): The number of spaces to use for indentation when pretty is True. Defaults to 1.

   Returns:
       str: The rendered HTML string.


