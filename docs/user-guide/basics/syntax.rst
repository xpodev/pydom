.. _syntax:

######
Syntax
######

PyDOM provides multiple syntaxes for creating instances of components.

It is recommended to pick one syntax and sticking to it, as mixing syntaxes on different components can lead to confusion.

Using the card component as an example, we will show the different syntaxes.

.. code-block:: python
    :caption: Card component
    
    # card.py

    from pydom import Component, Div

    class Card(Component):
        def __init__(self, title=None):
            self.title = title

        def render(self):
            return Div(classes="card")(
              self.title and Div(classes="card-title")(
                self.title
              ),
              Div(classes="card-content")(
                *self.children
              )
            )

Which will result in the following HTML when passing the title "Card Title" and the content "Hello, World!":

.. code-block:: html

    <div class="card">
      <div class="card-title">Card Title</div>
      <div class="card-content">Hello, World!</div>
    </div>

Pythonic Syntax
###############

Pass the children as positional arguments, and the props as keyword arguments.

This is called "Pythonic" because it is similar to how we write Python code.

.. code-block:: python
    :caption: Pythonic Syntax

    from pydom import Div, render
    from card import Card

    render(
      Card(
        Div( # This is the Card's child
          "Hello, World!", # This is the content of the Div
          id="card-content"
        ),
        title="Card Title"
      )
    )

HTML Syntax
###########

Start with the props as keyword arguments, then, pass the children as call arguments.

This is similar to how we write HTML tags, with the props as attributes and the children as the tag's content.

.. code-block:: python
    :caption: HTML Syntax

    from pydom import Div, render
    from card import Card

    render(
      Card(title="Card Title")(
        Div(id="card-content")( # This is the Card's child
          "Hello, World!" # This is the content of the Div
        )
      )
    )

Flutter Syntax
##############

Pass the children as the keyword argument "children", along with the props.

This is similar to how we write Flutter widgets.

.. code-block:: python
    :caption: Flutter Syntax  

    from pydom import Div, render
    from card import Card

    render(
      Card(
        title="Card Title",
        children=[Div( # This is the Card's child
          id="card-content".
          children=["Hello, World!"] # This is the content of the Div
        )]
      )
    )

.. note::

    When using the Flutter syntax, children must be passed as an iterable.

.. important::
  Using multiple syntaxes on the same component will not add the children together, each syntax will
  override the other, so stick to one syntax per component.

  The priority of the syntaxes is ``HTML`` > ``Flutter`` > ``Pythonic``, which means that if you pass
  children as call arguments, the children passed as keyword arguments will be ignored, and if you
  pass children as a keyword argument, the children passed as positional arguments will be ignored.