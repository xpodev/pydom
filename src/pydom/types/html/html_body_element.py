from pydom.types.html.html_element_props import HTMLElementProps


class HTMLBodyElement(HTMLElementProps, total=False, closed=False):
    alink: str
    """
    **@deprecated** Use the CSS color property in conjunction with the :active pseudo-class instead

    Specifies the color of text for hyperlinks when selected
    """
    background: str
    """
    **@deprecated** Use the CSS background property on the element instead

    Specifies the URI of an image to use as a background
    """
    bgcolor: str
    """
    **@deprecated** Use the CSS background-color property on the element instead

    Specifies the background color of the document
    """
    bottom_margin: int
    """
    **@deprecated** Use the CSS margin-bottom property on the element instead

    Specifies the bottom margin of the body
    """
    left_margin: int
    """
    **@deprecated** Use the CSS margin-left property on the element instead

    Specifies the left margin of the body
    """
    link: str
    """
    **@deprecated** Use the CSS color property in conjunction with the :link pseudo-class instead

    Specifies the color of text for unvisited hypertext links
    """
    on_after_print: str
    """
    Function to call after the user has printed the document
    """
    on_before_print: str
    """
    Function to call before the user prints the document
    """
    on_before_unload: str
    """
    Function to call when the document is about to be unloaded
    """
    on_hash_change: str
    """
    Function to call when the fragment identifier part (starting with the hash (`#`) character)
    of the document's current address has changed
    """
    on_language_change: str
    """
    Function to call when the preferred languages changed
    """
    on_message: str
    """
    Function to call when the document has received a message
    """
    on_offline: str
    """
    Function to call when network communication has failed
    """
    on_online: str
    """
    Function to call when network communication has been restored
    """
    on_pop_state: str
    """
    Function to call when the user has navigated session history
    """
    on_storage: str
    """
    Function to call when the storage area has changed
    """
    on_unload: str
    """
    Function to call when the document is going away
    """
    right_margin: int
    """
    **@deprecated** Use the CSS margin-right property on the element instead

    Specifies the right margin of the body
    """
    text: str
    """
    **@deprecated** Use the CSS color property on the element instead

    Specifies the color of text
    """
    top_margin: int
    """
    **@deprecated** Use the CSS margin-top property on the element instead

    Specifies the top margin of the body
    """
    vlink: str
    """
    **@deprecated** Use the CSS color property in conjunction with the :visited pseudo-class instead

    Specifies the color of text for visited hypertext links
    """
