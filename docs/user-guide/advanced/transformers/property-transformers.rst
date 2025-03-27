.. _property-transformers:

#####################
Property Transformers
#####################

Property transformers are used to transform a specific attribute of an element.
For example, you can use a property transformer to give a class to each element that has inline styles.

.. note:: 
    Property transformers are only available for elements and not for components.
    This is because property transformers are applied after the whole component is rendered to a normalized tree.

Property Transformers can be function or class-based.

Function Based Property Transformers
####################################

The function-based transformers are simple functions that take the property name, value, element, and render state as arguments.

After the function is defined, you can use the :func:`property_transformer <pydom.rendering.transformers.property_transformer>` decorator to register the transformer.
The decorator takes the property name as an argument or a :type:`matcher function <pydom.rendering.transformers.property_transformer.PropertyMatcherFunction>` that returns ``True`` if the transformer should be applied.

The following example demonstrates how to use a property transformer to give a class to each element that has inline styles.

.. code-block:: python
    :caption: Property transformer to give a class to each element that has inline styles
    :name: property-transformer-example

    from pydom import Component, Div, Span
    from pydom.rendering.transformers import property_transformer
    from pydom.rendering.render_state import RenderState
    from pydom.rendering.tree.nodes import ContextNode

    @property_transformer("style")
    def add_class_to_inline_styles(key, value, element: ContextNode, render_state: RenderState):
        class_name = uuid4().hex
        if value:
            element.props["class"] = f"{class_name} {element.props.get('class', '')}"

        render_state.custom_data["my_transformer.css_string"] = render_state.custom_data.get("my_transformer.css_string", "") + f".{class_name} {{{value}}}"
        del element.props[key]


Class Based Property Transformers
#################################

The class-based transformers are classes that inherit from the :class:`PropertyTransformer <pydom.rendering.transformers.PropertyTransformer>`
class and implement the ``match`` and ``transform`` methods.

The ``match`` method should return ``True`` if the transformer should be applied.

The ``transform`` method takes the property name, value, element, and render state as arguments.

There are a few advantages to using class-based transformers:

- You can store state in the transformer class.
- You can access the transformer instance from the context after the transformer is registered.

Like the :ref:`previous example <property-transformer-example>`, the following example demonstrates how to use a class-based property transformer to give a class to each element that has inline styles.

.. code-block:: python
    :caption: Class-based property transformer to give a class to each element that has inline styles

    from pydom import Component, Div, Span
    from pydom.rendering.transformers import PropertyTransformer
    from pydom.rendering.tree.nodes import ContextNode
    from pydom.rendering.render_state import RenderState

    class AddClassToInlineStyles(PropertyTransformer):
        def match(self, key, value, element: ContextNode) -> bool:
            return key == "style"

        def transform(self, key, value, element: ContextNode, render_state: RenderState) -> None:
            class_name = uuid4().hex
            if value:
                element.props["class"] = f"{class_name} {element.props.get('class', '')}"

            render_state.custom_data["my_transformer.css_string"] = render_state.custom_data.get("my_transformer.css_string", "") + f".{class_name} {{{value}}}"
            del element.props[key]

.. note::
    Property transformers can access injected properties from the context.


Registering Property Transformers
#################################

To register a property transformer, you need to add it to the context.

This can be done in two ways:

1. By using the :meth:`add_prop_transformer <pydom.context.Context.add_prop_transformer>` method of the context.
2. By using the :func:`property_transformer <pydom.rendering.transformers.property_transformer>` decorator - this applied only to function-based transformers.

The following code demonstrates how to register the property transformer from the :ref:`previous example <property-transformer-example>`:

.. code-block:: python
    :caption: Registering the property transformer

    from pydom import get_context

    get_context().add_prop_transformer(add_class_to_inline_styles)
    get_context().add_prop_transformer(AddClassToInlineStyles())

When adding a class-based transformer make sure to instantiate the class before adding it to the context.

Both ``add_prop_transformer`` and the decorator take optional ``before`` and ``after`` arguments that specifies
the order in which the transformers should be applied.
This can be useful when you need to ensure that a transformer is applied before or after another transformer.
Both arguments accept a list of transformer types. Passing a function-based transformer inside the list will not take effect.
