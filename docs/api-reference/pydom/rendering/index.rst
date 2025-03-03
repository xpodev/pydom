pydom.rendering
===============

.. py:module:: pydom.rendering


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/rendering/html/index
   /api-reference/pydom/rendering/json/index
   /api-reference/pydom/rendering/props/index
   /api-reference/pydom/rendering/render_state/index
   /api-reference/pydom/rendering/transformers/index
   /api-reference/pydom/rendering/tree/index


Functions
---------

.. autoapisummary::

   pydom.rendering.render_html
   pydom.rendering.render_json
   pydom.rendering.render


Package Contents
----------------

.. py:function:: render_html(element: pydom.types.RenderResult, *, context: Optional[pydom.context.Context] = None, pretty=False, tab_indent=1, **render_state_data) -> str

   Renders the given element into an HTML string.

   Args:
       element (Renderable | Primitive): The element to be rendered.
       pretty (bool, optional): Whether to format the HTML string with indentation and line breaks. Defaults to False.
       tab_indent (int, optional): The number of spaces to use for indentation when pretty is True. Defaults to 1.

   Returns:
       str: The rendered HTML string.


.. py:function:: render_json(element: pydom.types.RenderResult, *, context: Optional[pydom.context.Context] = None, **render_state_data)

.. py:function:: render(element: Union[pydom.types.Renderable, pydom.types.Primitive], *, to: Literal['html'], pretty: bool = False, tab_indent: int = 1, context: Optional[pydom.context.Context] = None, **render_state_data) -> str
                 render(element: Union[pydom.types.Renderable, pydom.types.Primitive], *, to: Literal['json'], context: Optional[pydom.context.Context] = None, **render_state_data) -> pydom.types.rendering.RenderResultJSON
                 render(element: Union[pydom.types.Renderable, pydom.types.Primitive], *, pretty: bool = False, tab_indent: int = 1, context: Optional[pydom.context.Context] = None, **render_state_data) -> str

