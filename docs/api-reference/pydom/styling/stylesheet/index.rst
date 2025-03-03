pydom.styling.stylesheet
========================

.. py:module:: pydom.styling.stylesheet


Attributes
----------

.. autoapisummary::

   pydom.styling.stylesheet.T


Classes
-------

.. autoapisummary::

   pydom.styling.stylesheet.StyleSheet


Module Contents
---------------

.. py:data:: T

.. py:class:: StyleSheet(*styles: Union[StyleSheet, pydom.types.styling.css_properties.CSSProperties], **kwargs: typing_extensions.Unpack[pydom.types.styling.css_properties.CSSProperties])

   .. py:attribute:: style
      :type:  Dict[str, object]


   .. py:method:: copy()


   .. py:method:: to_css()


   .. py:method:: __str__()


   .. py:method:: __getattr__(name: str)


