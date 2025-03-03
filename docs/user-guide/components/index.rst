.. _components:

##########
Components
##########

In HTML, there are tags like ``div``, ``span``, ``input``, ``button``, which describe the structure of the UI.

Elements are represented by classes like :class:`Div <pydom.Div>`, :class:`Span <pydom.Span>`,
:class:`Input <pydom.Input>`, :class:`Button <pydom.Button>`, which are subclasses of the
:class:`Element <pydom.element.Element>` class.

Components are subclasses of the base :class:`Component <pydom.component.Component>` class and are used to create reusable
and more complex UI structures.

For example, an ``AppButton`` component can be created which can be used throughout the application.

To create a component, create a class which inherits from ``Component`` class and define the
``render`` method which returns the ``Element`` or ``Component`` which will be rendered.

The :meth:`render <pydom.Component.render>` method can return a single ``Element``, ``Component``
or one of the :type:`primitive <pydom.type.Primitive>` types:

- str
- int
- float
- bool
- None

Except for the actual return value which can be only single ``Element``, ``Component`` or one of the primitive types, components and elements can have any number of children.
To return multiple components from the ``render`` method, use the :ref:`fragment` component.

.. toctree::
    :hidden:

    base-component
    page
    fragment