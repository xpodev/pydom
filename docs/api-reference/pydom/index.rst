pydom
=====

.. py:module:: pydom


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/cli/index
   /api-reference/pydom/component/index
   /api-reference/pydom/context/index
   /api-reference/pydom/element/index
   /api-reference/pydom/errors/index
   /api-reference/pydom/page/index
   /api-reference/pydom/rendering/index
   /api-reference/pydom/styling/index
   /api-reference/pydom/types/index
   /api-reference/pydom/version/index


Attributes
----------

.. autoapisummary::

   pydom.__version__


Classes
-------

.. autoapisummary::

   pydom.Component
   pydom.Context
   pydom.A
   pydom.Abbr
   pydom.Address
   pydom.Area
   pydom.Article
   pydom.Aside
   pydom.B
   pydom.Base
   pydom.BlockQuote
   pydom.Body
   pydom.Br
   pydom.Button
   pydom.Canvas
   pydom.Cite
   pydom.Code
   pydom.Col
   pydom.Div
   pydom.Em
   pydom.Embed
   pydom.Footer
   pydom.Form
   pydom.Fragment
   pydom.H1
   pydom.H2
   pydom.H3
   pydom.H4
   pydom.H5
   pydom.H6
   pydom.Head
   pydom.Header
   pydom.Hr
   pydom.Html
   pydom.I
   pydom.Img
   pydom.Input
   pydom.Label
   pydom.Li
   pydom.Link
   pydom.Main
   pydom.Meta
   pydom.Nav
   pydom.Ol
   pydom.Option
   pydom.P
   pydom.Param
   pydom.Pre
   pydom.Script
   pydom.Section
   pydom.Select
   pydom.Small
   pydom.Source
   pydom.Span
   pydom.Strong
   pydom.Style
   pydom.Sub
   pydom.Sup
   pydom.Table
   pydom.TBody
   pydom.Td
   pydom.TextArea
   pydom.Th
   pydom.THead
   pydom.Time
   pydom.Title
   pydom.Tr
   pydom.Track
   pydom.U
   pydom.Ul
   pydom.Wbr
   pydom.Page
   pydom.SvgA
   pydom.Animate
   pydom.AnimateMotion
   pydom.AnimateTransform
   pydom.Circle
   pydom.ClipPath
   pydom.Defs
   pydom.Desc
   pydom.Ellipse
   pydom.FeBlend
   pydom.FeColorMatrix
   pydom.FeComponentTransfer
   pydom.FeComposite
   pydom.FeConvolveMatrix
   pydom.FeDiffuseLighting
   pydom.FeDisplacementMap
   pydom.FeDistantLight
   pydom.FeDropShadow
   pydom.FeFlood
   pydom.FeFuncA
   pydom.FeFuncB
   pydom.FeFuncG
   pydom.FeFuncR
   pydom.FeGaussianBlur
   pydom.FeImage
   pydom.FeMerge
   pydom.FeMergeNode
   pydom.FeMorphology
   pydom.FeOffset
   pydom.FePointLight
   pydom.FeSpecularLighting
   pydom.FeSpotLight
   pydom.FeTile
   pydom.FeTurbulence
   pydom.Filter
   pydom.ForeignObject
   pydom.G
   pydom.Image
   pydom.Line
   pydom.LinearGradient
   pydom.Marker
   pydom.Mask
   pydom.Metadata
   pydom.MPath
   pydom.Path
   pydom.Pattern
   pydom.Polygon
   pydom.Polyline
   pydom.RadialGradient
   pydom.Rect
   pydom.SvgScript
   pydom.Set
   pydom.Stop
   pydom.SvgStyle
   pydom.Svg
   pydom.Switch
   pydom.Symbol
   pydom.Text
   pydom.TextPath
   pydom.Title
   pydom.TSpan
   pydom.Use
   pydom.View


Functions
---------

.. autoapisummary::

   pydom.render


Package Contents
----------------

.. py:class:: Component(*children: pydom.types.rendering.ChildType)

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: children
      :type:  Tuple[pydom.types.rendering.ChildType, Ellipsis]


   .. py:method:: render(*_, **kwargs) -> pydom.types.rendering.RenderResult
      :abstractmethod:



   .. py:method:: __init_subclass__(**kwargs) -> None
      :classmethod:



   .. py:method:: __call__(*children: pydom.types.rendering.ChildType)


.. py:class:: Context

   .. py:attribute:: injector
      :type:  pydom.utils.injector.Injector


   .. py:method:: add_prop_transformer(transformer: pydom.rendering.transformers.PropertyTransformer, /, *, before: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None) -> None
                  add_prop_transformer(matcher: pydom.rendering.transformers.property_transformer.PropertyMatcherFunction, transformer: pydom.rendering.transformers.property_transformer.PropertyTransformerFunction, /, *, before: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None, after: Optional[List[Type[pydom.rendering.transformers.PropertyTransformer]]] = None) -> None


   .. py:method:: add_post_render_transformer(transformer: Union[pydom.rendering.transformers.post_render_transformer.PostRenderTransformerFunction, pydom.rendering.transformers.PostRenderTransformer], /, *, before: Optional[List[Type[pydom.rendering.transformers.PostRenderTransformer]]] = None, after: Optional[List[Type[pydom.rendering.transformers.PostRenderTransformer]]] = None)


   .. py:property:: prop_transformers


   .. py:property:: post_render_transformers


   .. py:method:: inject(callback: Callable) -> Callable


   .. py:method:: standard() -> typing_extensions.Self
      :classmethod:



.. py:class:: A(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLAnchorElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'a'



.. py:class:: Abbr(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'abbr'



.. py:class:: Address(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'address'



.. py:class:: Area(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLAreaElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'area'



   .. py:attribute:: inline
      :value: True



.. py:class:: Article(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'article'



.. py:class:: Aside(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'aside'



.. py:class:: B(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'b'



.. py:class:: Base(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLBaseElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'base'



   .. py:attribute:: inline
      :value: True



.. py:class:: BlockQuote(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'blockquote'



.. py:class:: Body(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLBodyElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'body'



.. py:class:: Br(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLBRElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'br'



   .. py:attribute:: inline
      :value: True



.. py:class:: Button(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLButtonElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'button'



.. py:class:: Canvas(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLCanvasElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'canvas'



.. py:class:: Cite(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'cite'



.. py:class:: Code(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'code'



.. py:class:: Col(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableColElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'col'



   .. py:attribute:: inline
      :value: True



.. py:class:: Div(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLDivElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'div'



.. py:class:: Em(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'em'



.. py:class:: Embed(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLEmbedElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'embed'



   .. py:attribute:: inline
      :value: True



.. py:class:: Footer(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'footer'



.. py:class:: Form(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLFormElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'form'



.. py:class:: Fragment(*args: pydom.types.rendering.ChildType, children: Optional[pydom.types.rendering.ChildrenType] = None, **kwargs: typing_extensions.Unpack[PropsType])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: ''



.. py:class:: H1(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'h1'



.. py:class:: H2(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'h2'



.. py:class:: H3(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'h3'



.. py:class:: H4(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'h4'



.. py:class:: H5(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'h5'



.. py:class:: H6(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'h6'



.. py:class:: Head(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHeadElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'head'



.. py:class:: Header(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'header'



.. py:class:: Hr(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHRElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'hr'



   .. py:attribute:: inline
      :value: True



.. py:class:: Html(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLHtmlElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'html'



.. py:class:: I(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'i'



.. py:class:: Img(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLImageElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'img'



   .. py:attribute:: inline
      :value: True



.. py:class:: Input(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLInputElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'input'



   .. py:attribute:: inline
      :value: True



.. py:class:: Label(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLLabelElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'label'



.. py:class:: Li(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLListItemElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'li'



.. py:class:: Link(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLLinkElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'link'



   .. py:attribute:: inline
      :value: True



.. py:class:: Main(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'main'



.. py:class:: Meta(*children: pydom.types.ChildType, http_equiv: HttpEquivOptions, content: str)
              Meta(*children: pydom.types.ChildType, name: str, content: str)
              Meta(*children: pydom.types.ChildType, charset: str)
              Meta(*children: pydom.types.ChildType, itemprop: str)

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'meta'



   .. py:attribute:: inline
      :value: True



.. py:class:: Nav(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'nav'



.. py:class:: Ol(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLOrderedListElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'ol'



.. py:class:: Option(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLOptionElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'option'



.. py:class:: P(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLParagraphElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'p'



.. py:class:: Param(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLParamElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'param'



   .. py:attribute:: inline
      :value: True



.. py:class:: Pre(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLPreElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'pre'



.. py:class:: Script(*children: str, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLScriptElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'script'



   .. py:attribute:: escape_children
      :value: False



.. py:class:: Section(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'section'



.. py:class:: Select(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLSelectElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'select'



.. py:class:: Small(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'small'



.. py:class:: Source(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLSourceElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'source'



   .. py:attribute:: inline
      :value: True



.. py:class:: Span(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLSpanElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'span'



.. py:class:: Strong(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'strong'



.. py:class:: Style(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLStyleElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'style'



   .. py:attribute:: escape_children
      :value: False



.. py:class:: Sub(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'sub'



.. py:class:: Sup(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'sup'



.. py:class:: Table(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'table'



.. py:class:: TBody(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableSectionElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'tbody'



.. py:class:: Td(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableDataCellElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'td'



.. py:class:: TextArea(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTextAreaElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'textarea'



.. py:class:: Th(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableHeaderCellElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'th'



.. py:class:: THead(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableSectionElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'thead'



.. py:class:: Time(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTimeElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'time'



.. py:class:: Title(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTitleElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'title'



.. py:class:: Tr(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTableRowElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'tr'



.. py:class:: Track(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLTrackElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'track'



   .. py:attribute:: inline
      :value: True



.. py:class:: U(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'u'



.. py:class:: Ul(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLUnorderedListElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'ul'



.. py:class:: Wbr(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.html.HTMLElementProps])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'wbr'



   .. py:attribute:: inline
      :value: True



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



.. py:class:: SvgA(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGAnchorElement])

   Bases: :py:obj:`pydom.element.Element`


   The SVG <a> element provides a way to create hyperlinks within SVG content. It supports any SVG element or graphics element.

   :Notice: The SVG <a> element is not the same as the HTML <a> element. The SVG <a> element is a container for graphics, while the HTML <a> element is a hypertext link.


   .. py:attribute:: tag_name
      :value: 'a'



.. py:class:: Animate(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGAnimateElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'animate'



.. py:class:: AnimateMotion(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGAnimateMotionElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'animatemotion'



.. py:class:: AnimateTransform(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGAnimateTransformElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'animatetransform'



.. py:class:: Circle(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGCircleElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'circle'



.. py:class:: ClipPath(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGClipPathElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'clippath'



.. py:class:: Defs(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGDefsElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'defs'



.. py:class:: Desc(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGDescElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'desc'



.. py:class:: Ellipse(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGEllipseElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'ellipse'



.. py:class:: FeBlend(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEBlendElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'feblend'



.. py:class:: FeColorMatrix(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEColorMatrixElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fecolormatrix'



.. py:class:: FeComponentTransfer(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEComponentTransferElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fecomponenttransfer'



.. py:class:: FeComposite(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFECompositeElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fecomposite'



.. py:class:: FeConvolveMatrix(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEConvolveMatrixElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'feconvolvematrix'



.. py:class:: FeDiffuseLighting(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEDiffuseLightingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fediffuselighting'



.. py:class:: FeDisplacementMap(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEDisplacementMapElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fedisplacementmap'



.. py:class:: FeDistantLight(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEDistantLightElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fedistantlight'



.. py:class:: FeDropShadow(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEDropShadowElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fedropshadow'



.. py:class:: FeFlood(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEFloodElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'feflood'



.. py:class:: FeFuncA(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEFuncAElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fefunca'



.. py:class:: FeFuncB(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEFuncBElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fefuncb'



.. py:class:: FeFuncG(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEFuncGElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fefuncg'



.. py:class:: FeFuncR(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEFuncRElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fefuncr'



.. py:class:: FeGaussianBlur(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEGaussianBlurElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fegaussianblur'



.. py:class:: FeImage(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEImageElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'feimage'



.. py:class:: FeMerge(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEMergeElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'femerge'



.. py:class:: FeMergeNode(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEMergeNodeElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'femergenode'



.. py:class:: FeMorphology(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEMorphologyElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'femorphology'



.. py:class:: FeOffset(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEOffsetElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'feoffset'



.. py:class:: FePointLight(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFEPointLightElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fepointlight'



.. py:class:: FeSpecularLighting(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFESpecularLightingElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fespecularlighting'



.. py:class:: FeSpotLight(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFESpotLightElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fespotlight'



.. py:class:: FeTile(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFETileElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'fetile'



.. py:class:: FeTurbulence(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFETurbulenceElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'feturbulence'



.. py:class:: Filter(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGFilterElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'filter'



.. py:class:: ForeignObject(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGForeignObjectElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'foreignobject'



.. py:class:: G(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGGElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'g'



.. py:class:: Image(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGImageElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'image'



.. py:class:: Line(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGLineElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'line'



.. py:class:: LinearGradient(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGLinearGradientElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'lineargradient'



.. py:class:: Marker(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGMarkerElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'marker'



.. py:class:: Mask(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGMaskElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'mask'



.. py:class:: Metadata(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGMetadataElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'metadata'



.. py:class:: MPath(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGMPathElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'mpath'



.. py:class:: Path(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGPathElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'path'



.. py:class:: Pattern(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGPatternElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'pattern'



.. py:class:: Polygon(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGPolygonElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'polygon'



.. py:class:: Polyline(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGPolylineElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'polyline'



.. py:class:: RadialGradient(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGRadialGradientElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'radialgradient'



.. py:class:: Rect(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGRectElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'rect'



.. py:class:: SvgScript(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGScriptElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'script'



.. py:class:: Set(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGSetElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'set'



.. py:class:: Stop(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGStopElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'stop'



.. py:class:: SvgStyle(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGStyleElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'style'



.. py:class:: Svg(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGSVGElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'svg'



.. py:class:: Switch(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGSwitchElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'switch'



.. py:class:: Symbol(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGSymbolElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'symbol'



.. py:class:: Text(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGTextElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'text'



.. py:class:: TextPath(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGTextPathElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'textpath'



.. py:class:: Title(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGTitleElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'title'



.. py:class:: TSpan(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGTSpanElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'tspan'



.. py:class:: Use(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGUseElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'use'



.. py:class:: View(*children: pydom.types.ChildType, **kwargs: typing_extensions.Unpack[pydom.types.svg.SVGViewElement])

   Bases: :py:obj:`pydom.element.Element`


   .. py:attribute:: tag_name
      :value: 'view'



.. py:function:: render(element: Union[pydom.types.Renderable, pydom.types.Primitive], *, to: Literal['html'], pretty: bool = False, tab_indent: int = 1, context: Optional[pydom.context.Context] = None, **render_state_data) -> str
                 render(element: Union[pydom.types.Renderable, pydom.types.Primitive], *, to: Literal['json'], context: Optional[pydom.context.Context] = None, **render_state_data) -> pydom.types.rendering.RenderResultJSON
                 render(element: Union[pydom.types.Renderable, pydom.types.Primitive], *, pretty: bool = False, tab_indent: int = 1, context: Optional[pydom.context.Context] = None, **render_state_data) -> str

.. py:data:: __version__
   :value: '0.3.1'


