pydom.page
==========

.. py:module:: pydom.page


Classes
-------

.. autoapisummary::

   pydom.page.Page


Module Contents
---------------

.. py:class:: Page(*children: pydom.types.ChildType, title: Optional[str] = None, html_props: Optional[pydom.types.html.HTMLHtmlElement] = None, head_props: Optional[pydom.types.html.HTMLHeadElement] = None, body_props: Optional[pydom.types.html.HTMLBodyElement] = None)
              Page(*, children: pydom.types.ChildrenType, title: Optional[str] = None, html_props: Optional[pydom.types.html.HTMLHtmlElement] = None, head_props: Optional[pydom.types.html.HTMLHeadElement] = None, body_props: Optional[pydom.types.html.HTMLBodyElement] = None)

   Bases: :py:obj:`pydom.component.Component`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: title
      :value: None



   .. py:method:: head() -> Iterable[pydom.types.ChildType]

      The children that will be inside the `head` tag.



   .. py:method:: body() -> Iterable[pydom.types.ChildType]

      The children that will be inside the `body` tag.



   .. py:method:: render()


   .. py:method:: __init_subclass__(title: Optional[str] = None, **kwargs) -> None
      :classmethod:



