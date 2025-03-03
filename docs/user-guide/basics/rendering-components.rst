.. _rendering-components:

####################
Rendering Components
####################

HTML Rendering
##############

To convert components to the HTML representation, use the :func:`render <pydom.render>` method.
This method returns a string containing the HTML representation of the component.
For example, to render a page with the :ref:`card-component` component, you can use the following code:

.. code-block:: python
    :caption: Rendering the page as HTML

    from pydom import render
    from pydom.components import Page
    from card import Card

    card = Card(title="Card Title")(
        "This is the content of the card"
    )

    html = render(Page(card))

    print(html)

This will output the following HTML:

.. code-block:: html
    :caption: HTML render result

    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body dir="ltr">
            <div class="card">
                <div class="card-title">
                    Card Title
                </div>
                <div class="card-content">
                    This is the content of the card
                </div>
            </div>
        </body>
    </html>

The ``render`` method can pretty-print the HTML by setting the ``pretty`` parameter to ``True``.

JSON Rendering
##############

To convert components to the JSON representation, use the ``to_dict`` method from ``pydom.renderer``.
This method returns a dict containing the JSON representation of the component.

.. code-block:: python
    :caption: Rendering the page as JSON

    from json import dumps
    from pydom.renderer import to_dict
    from card import Card

    card = Card(title="Card Title")(
        "This is the content of the card"
    )

    json = to_dict(card)

    print(dumps(json))

This will output the following JSON:

.. code-block:: json
    :caption: JSON representation of the page

    {
      "type": "div",
      "children": [
        {
          "type": "div",
          "children": [
            "Card Title"
          ],
          "props": {
            "class": "card-title"
          }
        },
        {
          "type": "div",
          "children": [
            "This is the content of the card"
          ],
          "props": {
            "class": "card-content"
          }
        }
      ],
      "props": {
        "class": "card"
      }
    }

This dict can be used to render components on the client side after the initial server-side rendering.

It also corresponds to React's virtual DOM representation of the component.

.. _props-rendering:

Props Rendering
###############

When rendering components, some props names are converted to another name in the HTML representation.
For example, the ``classes`` prop is converted to the ``class`` attribute in the HTML representation.

The full list of prop names and their corresponding HTML attributes is as follows:

- ``classes`` -> ``class``
- ``html_for`` -> ``for``
- ``access_key`` -> ``accesskey``
- ``content_editable`` -> ``contenteditable``
- ``cross_origin`` -> ``crossorigin``
- ``tab_index`` -> ``tabindex``
- ``use_map`` -> ``usemap``
- ``col_span`` -> ``colspan``
- ``row_span`` -> ``rowspan``
- ``char_set`` -> ``charset``

By default, all props with underscore in their name and a value of :py:type:`~pydom.types.Primitive` type,
are converted to HTML attributes with dash instead of underscore.

To configure this behavior check out the :ref:`property-transformers` page.
