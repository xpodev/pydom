.. _fragment:

########
Fragment
########

``Fragment`` is an empty element that can be used to wrap a list of elements. It is a common pattern
in PyDOM to return multiple elements from a component without adding an extra node to the DOM.

.. code-block:: python
    :caption: Using Fragment

    from pydom import Fragment, Component, Div

    class MyComponent(Component):
        def render(self):
            return Fragment(
                Div("Hello"),
                Div("World")
            )

.. note::

    Even though it's under the :ref:`components` section, ``Fragment`` is not a component itself but an element,
    which means transformers can be applied to it.