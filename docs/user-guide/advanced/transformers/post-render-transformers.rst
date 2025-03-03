.. _post-render-transformers:

########################
Post-Render Transformers
########################

Post-render transformers are used to transform the entire HTML content after it is rendered.

Like property transformers, post-render transformers can be function or class-based.

Function Based Post-Render Transformers
#######################################

The function-based transformers are simple functions that take the root element and render state as arguments.

After the function is defined, you can use the :func:`post_render_transformer <pydom.rendering.transformers.post_render_transformer>` decorator to register the transformer.

The following example demonstrates how to use a post-render transformer to add the CSS from the :ref:`property transformer <property-transformer-example>` to the HTML content:

.. code-block:: python
    :caption: Using a post-render transformer to add the CSS from the property transformer to the HTML content

    from pydom.rendering.transformers import post_render_transformer

    from pydom.rendering.render_state import RenderState
    from pydom.rendering.tree.nodes import ElementNode


    @post_render_transformer()
    def add_css_to_html(root: ElementNode, render_state: RenderState):
        if "my_transformer.css_string" not in render_state.custom_data:
            return

        root.get_by_tag("head").append(
            ElementNode(
                tag_name="style",
                children=[render_state.custom_data["my_transformer.css_string"]]
            )
        )

Class Based Post-Render Transformers
####################################

The class-based transformers are classes that inherit from the :class:`PostRenderTransformer <pydom.content.transformers.PostRenderTransformer>`

There are a few advantages to using class-based transformers:

- You can store state in the transformer class.
- You can access the transformer instance from the context after the transformer is registered.

The following example demonstrates how to use a post-render transformer to add the CSS from the :ref:`property transformer <property-transformer-example>`
to the HTML content:

.. code-block:: python
    :caption: Class-based post-render transformer to add the CSS from the property transformer to the HTML content

    from pydom.rendering.transformers import PostRenderTransformer

    from pydom.rendering.render_state import RenderState
    from pydom.rendering.tree.nodes import ElementNode


    class AddCssToHtml(PostRenderTransformer):
        def transform(self, root: ElementNode, render_state: RenderState):
            if "my_transformer.css_string" not in render_state.custom_data:
                return

            root.get_by_tag("head").append(
                ElementNode(
                    tag_name="style",
                    children=[render_state.custom_data["my_transformer.css_string"]]
                )
            )


Registering Post-Render Transformers
####################################

To register a post-render transformer, you need to add it to the context.

This can be done in two ways:

1. By using the :meth:`add_post_render_transformer <pydom.context.Context.add_post_render_transformer>` method of the context.
2. By using the :func:`post_render_transformer <pydom.rendering.transformers.post_render_transformer>` decorator - this applied only to function-based transformers.

The following code demonstrates how to register class-based and function-based post-render transformers:

.. code-block:: python
    :caption: Registering the post-render transformer

    from pydom import get_context

    get_context().add_post_render_transformer(add_css_to_html)
    get_context().add_post_render_transformer(AddCssToHtml())

When adding a class-based transformer make sure to instantiate the class before adding it to the context.

Both ``add_post_render_transformer`` and the decorator take optional ``before`` and ``after`` arguments that specifies
the order in which the transformers should be applied.
This can be useful when you need to ensure that a transformer is applied before or after another transformer.
Both arguments accept a list of post-render transformer types. Passing a function-based transformer inside the list will not take effect.
