class Error(Exception):
    """
    Base class for all pydom exceptions.
    """

    ...


class RenderError(Error):
    """
    Raised when an error occurs while rendering an element.
    """

    ...