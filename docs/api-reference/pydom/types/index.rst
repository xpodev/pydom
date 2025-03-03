pydom.types
===========

.. py:module:: pydom.types


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api-reference/pydom/types/element/index
   /api-reference/pydom/types/rendering/index
   /api-reference/pydom/types/styling/index
   /api-reference/pydom/types/svg/index


Attributes
----------

.. autoapisummary::

   pydom.types.ChildType
   pydom.types.ChildrenType
   pydom.types.Primitive
   pydom.types.Renderable
   pydom.types.RenderResult
   pydom.types.RenderTarget


Classes
-------

.. autoapisummary::

   pydom.types.AriaProps
   pydom.types.HTMLAnchorElement
   pydom.types.HTMLAreaElement
   pydom.types.HTMLAudioElement
   pydom.types.HTMLBaseElement
   pydom.types.HTMLBodyElement
   pydom.types.HTMLBRElement
   pydom.types.HTMLButtonElement
   pydom.types.HTMLCanvasElement
   pydom.types.HTMLCharsetMetaElement
   pydom.types.HTMLDataElement
   pydom.types.HTMLDataListElement
   pydom.types.HTMLDetailsElement
   pydom.types.HTMLDialogElement
   pydom.types.HTMLDivElement
   pydom.types.HTMLDocumentMetaElement
   pydom.types.HTMLElement
   pydom.types.HTMLElementProps
   pydom.types.HTMLEmbedElement
   pydom.types.HTMLEventProps
   pydom.types.HTMLFieldSetElement
   pydom.types.HTMLFormElement
   pydom.types.HTMLHeadElement
   pydom.types.HTMLHeadingElement
   pydom.types.HTMLHRElement
   pydom.types.HTMLHtmlElement
   pydom.types.HTMLIFrameElement
   pydom.types.HTMLImageElement
   pydom.types.HTMLInputElement
   pydom.types.HTMLLabelElement
   pydom.types.HTMLLegendElement
   pydom.types.HTMLLinkElement
   pydom.types.HTMLListItemElement
   pydom.types.HTMLMapElement
   pydom.types.HTMLMeterElement
   pydom.types.HTMLModElement
   pydom.types.HTMLObjectElement
   pydom.types.HTMLOptGroupElement
   pydom.types.HTMLOptionElement
   pydom.types.HTMLOrderedListElement
   pydom.types.HTMLOutputElement
   pydom.types.HTMLParagraphElement
   pydom.types.HTMLParamElement
   pydom.types.HTMLPictureElement
   pydom.types.HTMLPragmaMetaElement
   pydom.types.HTMLPreElement
   pydom.types.HTMLProgressElement
   pydom.types.HTMLQuoteElement
   pydom.types.HTMLScriptElement
   pydom.types.HTMLSelectElement
   pydom.types.HTMLSlotElement
   pydom.types.HTMLSourceElement
   pydom.types.HTMLSpanElement
   pydom.types.HTMLStyleElement
   pydom.types.HTMLTableCaptionElement
   pydom.types.HTMLTableCellElement
   pydom.types.HTMLTableColElement
   pydom.types.HTMLTableDataCellElement
   pydom.types.HTMLTableElement
   pydom.types.HTMLTableHeaderCellElement
   pydom.types.HTMLTableRowElement
   pydom.types.HTMLTableSectionElement
   pydom.types.HTMLTemplateElement
   pydom.types.HTMLTextAreaElement
   pydom.types.HTMLTimeElement
   pydom.types.HTMLTitleElement
   pydom.types.HTMLTrackElement
   pydom.types.HTMLUnorderedListElement
   pydom.types.HTMLUserMetaElement
   pydom.types.HTMLVideoElement
   pydom.types.RenderResultJSON
   pydom.types.CSSProperties


Package Contents
----------------

.. py:class:: AriaProps

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: aria_active_descendant
      :type:  Optional[str]


   .. py:attribute:: aria_atomic
      :type:  Optional[str]


   .. py:attribute:: aria_auto_complete
      :type:  Optional[str]


   .. py:attribute:: aria_busy
      :type:  Optional[str]


   .. py:attribute:: aria_checked
      :type:  Optional[str]


   .. py:attribute:: aria_col_count
      :type:  Optional[str]


   .. py:attribute:: aria_col_index
      :type:  Optional[str]


   .. py:attribute:: aria_col_span
      :type:  Optional[str]


   .. py:attribute:: aria_controls
      :type:  Optional[str]


   .. py:attribute:: aria_current
      :type:  Optional[str]


   .. py:attribute:: aria_described_by
      :type:  Optional[str]


   .. py:attribute:: aria_details
      :type:  Optional[str]


   .. py:attribute:: aria_disabled
      :type:  Optional[str]


   .. py:attribute:: aria_drop_effect
      :type:  Optional[str]


   .. py:attribute:: aria_error_message
      :type:  Optional[str]


   .. py:attribute:: aria_expanded
      :type:  Optional[str]


   .. py:attribute:: aria_flow_to
      :type:  Optional[str]


   .. py:attribute:: aria_grabbed
      :type:  Optional[str]


   .. py:attribute:: aria_has_popup
      :type:  Optional[str]


   .. py:attribute:: aria_hidden
      :type:  Optional[str]


   .. py:attribute:: aria_invalid
      :type:  Optional[str]


   .. py:attribute:: aria_key_shortcuts
      :type:  Optional[str]


   .. py:attribute:: aria_label
      :type:  Optional[str]


   .. py:attribute:: aria_labelled_by
      :type:  Optional[str]


   .. py:attribute:: aria_level
      :type:  Optional[str]


   .. py:attribute:: aria_live
      :type:  Optional[str]


   .. py:attribute:: aria_modal
      :type:  Optional[str]


   .. py:attribute:: aria_multiline
      :type:  Optional[str]


   .. py:attribute:: aria_multi_selectable
      :type:  Optional[str]


   .. py:attribute:: aria_orientation
      :type:  Optional[str]


   .. py:attribute:: aria_owns
      :type:  Optional[str]


   .. py:attribute:: aria_placeholder
      :type:  Optional[str]


   .. py:attribute:: aria_pos_inset
      :type:  Optional[str]


   .. py:attribute:: aria_pressed
      :type:  Optional[str]


   .. py:attribute:: aria_readonly
      :type:  Optional[str]


   .. py:attribute:: aria_relevant
      :type:  Optional[str]


   .. py:attribute:: aria_required
      :type:  Optional[str]


   .. py:attribute:: aria_role_description
      :type:  Optional[str]


   .. py:attribute:: aria_row_count
      :type:  Optional[str]


   .. py:attribute:: aria_row_index
      :type:  Optional[str]


   .. py:attribute:: aria_row_span
      :type:  Optional[str]


   .. py:attribute:: aria_selected
      :type:  Optional[str]


   .. py:attribute:: aria_set_size
      :type:  Optional[str]


   .. py:attribute:: aria_sort
      :type:  Optional[str]


   .. py:attribute:: aria_value_max
      :type:  Optional[str]


   .. py:attribute:: aria_value_min
      :type:  Optional[str]


   .. py:attribute:: aria_value_now
      :type:  Optional[str]


   .. py:attribute:: aria_value_text
      :type:  Optional[str]


.. py:class:: HTMLAnchorElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: download
      :type:  Optional[str]


   .. py:attribute:: href
      :type:  Optional[str]


   .. py:attribute:: href_lang
      :type:  Optional[str]


   .. py:attribute:: ping
      :type:  Optional[str]


   .. py:attribute:: referrer_policy
      :type:  Optional[str]


   .. py:attribute:: rel
      :type:  Optional[str]


   .. py:attribute:: target
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


.. py:class:: HTMLAreaElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: alt
      :type:  Optional[str]


   .. py:attribute:: coords
      :type:  Optional[str]


   .. py:attribute:: download
      :type:  Optional[str]


   .. py:attribute:: href
      :type:  Optional[str]


   .. py:attribute:: href_lang
      :type:  Optional[str]


   .. py:attribute:: ping
      :type:  Optional[str]


   .. py:attribute:: referrer_policy
      :type:  Optional[str]


   .. py:attribute:: rel
      :type:  Optional[str]


   .. py:attribute:: shape
      :type:  Optional[str]


   .. py:attribute:: target
      :type:  Optional[str]


.. py:class:: HTMLAudioElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: auto_play
      :type:  Optional[str]


   .. py:attribute:: controls
      :type:  Optional[str]


   .. py:attribute:: loop
      :type:  Optional[str]


   .. py:attribute:: muted
      :type:  Optional[str]


   .. py:attribute:: preload
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


.. py:class:: HTMLBaseElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: href
      :type:  Optional[str]


   .. py:attribute:: target
      :type:  Optional[str]


.. py:class:: HTMLBodyElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: alink
      :type:  Optional[str]

      **@deprecated** Use the CSS color property in conjunction with the :active pseudo-class instead

      Specifies the color of text for hyperlinks when selected



   .. py:attribute:: background
      :type:  Optional[str]

      **@deprecated** Use the CSS background property on the element instead

      Specifies the URI of an image to use as a background



   .. py:attribute:: bgcolor
      :type:  Optional[str]

      **@deprecated** Use the CSS background-color property on the element instead

      Specifies the background color of the document



   .. py:attribute:: bottom_margin
      :type:  Optional[int]

      **@deprecated** Use the CSS margin-bottom property on the element instead

      Specifies the bottom margin of the body



   .. py:attribute:: left_margin
      :type:  Optional[int]

      **@deprecated** Use the CSS margin-left property on the element instead

      Specifies the left margin of the body



   .. py:attribute:: link
      :type:  Optional[str]

      **@deprecated** Use the CSS color property in conjunction with the :link pseudo-class instead

      Specifies the color of text for unvisited hypertext links



   .. py:attribute:: on_after_print
      :type:  Optional[str]

      Function to call after the user has printed the document



   .. py:attribute:: on_before_print
      :type:  Optional[str]

      Function to call before the user prints the document



   .. py:attribute:: on_before_unload
      :type:  Optional[str]

      Function to call when the document is about to be unloaded



   .. py:attribute:: on_hash_change
      :type:  Optional[str]

      Function to call when the fragment identifier part (starting with the hash (`#`) character)
      of the document's current address has changed



   .. py:attribute:: on_language_change
      :type:  Optional[str]

      Function to call when the preferred languages changed



   .. py:attribute:: on_message
      :type:  Optional[str]

      Function to call when the document has received a message



   .. py:attribute:: on_offline
      :type:  Optional[str]

      Function to call when network communication has failed



   .. py:attribute:: on_online
      :type:  Optional[str]

      Function to call when network communication has been restored



   .. py:attribute:: on_pop_state
      :type:  Optional[str]

      Function to call when the user has navigated session history



   .. py:attribute:: on_storage
      :type:  Optional[str]

      Function to call when the storage area has changed



   .. py:attribute:: on_unload
      :type:  Optional[str]

      Function to call when the document is going away



   .. py:attribute:: right_margin
      :type:  Optional[int]

      **@deprecated** Use the CSS margin-right property on the element instead

      Specifies the right margin of the body



   .. py:attribute:: text
      :type:  Optional[str]

      **@deprecated** Use the CSS color property on the element instead

      Specifies the color of text



   .. py:attribute:: top_margin
      :type:  Optional[int]

      **@deprecated** Use the CSS margin-top property on the element instead

      Specifies the top margin of the body



   .. py:attribute:: vlink
      :type:  Optional[str]

      **@deprecated** Use the CSS color property in conjunction with the :visited pseudo-class instead

      Specifies the color of text for visited hypertext links



.. py:class:: HTMLBRElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


.. py:class:: HTMLButtonElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: auto_focus
      :type:  Optional[str]


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: form_action
      :type:  Optional[str]


   .. py:attribute:: form_enctype
      :type:  Optional[str]


   .. py:attribute:: form_method
      :type:  Optional[str]


   .. py:attribute:: form_no_validate
      :type:  Optional[str]


   .. py:attribute:: form_target
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLCanvasElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLCharsetMetaElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: charset
      :type:  Optional[str]


.. py:class:: HTMLDataElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLDataListElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


.. py:class:: HTMLDetailsElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: open
      :type:  Optional[str]


.. py:class:: HTMLDialogElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: open
      :type:  Optional[str]


.. py:class:: HTMLDivElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


.. py:class:: HTMLDocumentMetaElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: content
      :type:  Optional[str]


.. py:class:: HTMLElement

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: access_key
      :type:  Optional[str]


   .. py:attribute:: auto_capitalize
      :type:  Optional[str]


   .. py:attribute:: classes
      :type:  Optional[Union[str, Iterable[str]]]


   .. py:attribute:: content_editable
      :type:  Optional[str]


   .. py:attribute:: dangerously_set_inner_html
      :type:  Optional[Dict[Literal['__html'], str]]


   .. py:attribute:: dir
      :type:  Optional[Literal['ltr', 'rtl', 'auto']]


   .. py:attribute:: draggable
      :type:  Optional[str]


   .. py:attribute:: hidden
      :type:  Optional[str]


   .. py:attribute:: id
      :type:  Optional[str]


   .. py:attribute:: input_mode
      :type:  Optional[str]


   .. py:attribute:: lang
      :type:  Optional[str]


   .. py:attribute:: role
      :type:  Optional[str]


   .. py:attribute:: spell_check
      :type:  Optional[str]


   .. py:attribute:: style
      :type:  Optional[Union[str, pydom.styling.StyleSheet]]


   .. py:attribute:: tab_index
      :type:  Optional[str]


   .. py:attribute:: title
      :type:  Optional[str]


   .. py:attribute:: translate
      :type:  Optional[str]


.. py:class:: HTMLElementProps

   Bases: :py:obj:`pydom.types.html.html_element.HTMLElement`, :py:obj:`pydom.types.html.aria_props.AriaProps`, :py:obj:`pydom.types.html.html_event_props.HTMLEventProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLEmbedElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLEventProps

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: on_abort
      :type:  Optional[str]


   .. py:attribute:: on_auto_complete
      :type:  Optional[str]


   .. py:attribute:: on_auto_complete_error
      :type:  Optional[str]


   .. py:attribute:: on_blur
      :type:  Optional[str]


   .. py:attribute:: on_cancel
      :type:  Optional[str]


   .. py:attribute:: on_can_play
      :type:  Optional[str]


   .. py:attribute:: on_can_play_through
      :type:  Optional[str]


   .. py:attribute:: on_change
      :type:  Optional[str]


   .. py:attribute:: on_click
      :type:  Optional[str]


   .. py:attribute:: on_close
      :type:  Optional[str]


   .. py:attribute:: on_context_menu
      :type:  Optional[str]


   .. py:attribute:: on_cue_change
      :type:  Optional[str]


   .. py:attribute:: on_dbl_click
      :type:  Optional[str]


   .. py:attribute:: on_drag
      :type:  Optional[str]


   .. py:attribute:: on_drag_end
      :type:  Optional[str]


   .. py:attribute:: on_drag_enter
      :type:  Optional[str]


   .. py:attribute:: on_drag_leave
      :type:  Optional[str]


   .. py:attribute:: on_drag_over
      :type:  Optional[str]


   .. py:attribute:: on_drag_start
      :type:  Optional[str]


   .. py:attribute:: on_drop
      :type:  Optional[str]


   .. py:attribute:: on_duration_change
      :type:  Optional[str]


   .. py:attribute:: on_emptied
      :type:  Optional[str]


   .. py:attribute:: on_ended
      :type:  Optional[str]


   .. py:attribute:: on_error
      :type:  Optional[str]


   .. py:attribute:: on_focus
      :type:  Optional[str]


   .. py:attribute:: on_input
      :type:  Optional[str]


   .. py:attribute:: on_invalid
      :type:  Optional[str]


   .. py:attribute:: on_key_down
      :type:  Optional[str]


   .. py:attribute:: on_key_press
      :type:  Optional[str]


   .. py:attribute:: on_key_up
      :type:  Optional[str]


   .. py:attribute:: on_load
      :type:  Optional[str]


   .. py:attribute:: on_loaded_data
      :type:  Optional[str]


   .. py:attribute:: on_loaded_metadata
      :type:  Optional[str]


   .. py:attribute:: on_load_start
      :type:  Optional[str]


   .. py:attribute:: on_mouse_down
      :type:  Optional[str]


   .. py:attribute:: on_mouse_enter
      :type:  Optional[str]


   .. py:attribute:: on_mouse_leave
      :type:  Optional[str]


   .. py:attribute:: on_mouse_move
      :type:  Optional[str]


   .. py:attribute:: on_mouse_out
      :type:  Optional[str]


   .. py:attribute:: on_mouse_over
      :type:  Optional[str]


   .. py:attribute:: on_mouse_up
      :type:  Optional[str]


   .. py:attribute:: on_mouse_wheel
      :type:  Optional[str]


   .. py:attribute:: on_pause
      :type:  Optional[str]


   .. py:attribute:: on_play
      :type:  Optional[str]


   .. py:attribute:: on_playing
      :type:  Optional[str]


   .. py:attribute:: on_progress
      :type:  Optional[str]


   .. py:attribute:: on_rate_change
      :type:  Optional[str]


   .. py:attribute:: on_reset
      :type:  Optional[str]


   .. py:attribute:: on_resize
      :type:  Optional[str]


   .. py:attribute:: on_scroll
      :type:  Optional[str]


   .. py:attribute:: on_seeked
      :type:  Optional[str]


   .. py:attribute:: on_seeking
      :type:  Optional[str]


   .. py:attribute:: on_select
      :type:  Optional[str]


   .. py:attribute:: on_show
      :type:  Optional[str]


   .. py:attribute:: on_sort
      :type:  Optional[str]


   .. py:attribute:: on_stalled
      :type:  Optional[str]


   .. py:attribute:: on_submit
      :type:  Optional[str]


   .. py:attribute:: on_suspend
      :type:  Optional[str]


   .. py:attribute:: on_time_update
      :type:  Optional[str]


   .. py:attribute:: on_toggle
      :type:  Optional[str]


   .. py:attribute:: on_volume_change
      :type:  Optional[str]


   .. py:attribute:: on_waiting
      :type:  Optional[str]


.. py:class:: HTMLFieldSetElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


.. py:class:: HTMLFormElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: accept_charset
      :type:  Optional[str]


   .. py:attribute:: action
      :type:  Optional[str]


   .. py:attribute:: auto_complete
      :type:  Optional[str]


   .. py:attribute:: enctype
      :type:  Optional[str]


   .. py:attribute:: method
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: no_validate
      :type:  Optional[str]


   .. py:attribute:: target
      :type:  Optional[str]


.. py:class:: HTMLHeadElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: profile
      :type:  Optional[str]


.. py:class:: HTMLHeadingElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLHRElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLHtmlElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: version
      :type:  Optional[str]


   .. py:attribute:: xmlns
      :type:  Optional[str]


.. py:class:: HTMLIFrameElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: allow
      :type:  Optional[str]


   .. py:attribute:: allow_fullscreen
      :type:  Optional[str]


   .. py:attribute:: csp
      :type:  Optional[str]


   .. py:attribute:: frame_border
      :type:  Optional[str]


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: importance
      :type:  Optional[str]


   .. py:attribute:: loading
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: referrer_policy
      :type:  Optional[str]


   .. py:attribute:: sandbox
      :type:  Optional[str]


   .. py:attribute:: scrolling
      :type:  Optional[str]


   .. py:attribute:: seamless
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: srcdoc
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLImageElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: alt
      :type:  Optional[str]


   .. py:attribute:: cross_origin
      :type:  Optional[str]


   .. py:attribute:: decoding
      :type:  Optional[str]


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: importance
      :type:  Optional[str]


   .. py:attribute:: intrinsicsize
      :type:  Optional[str]


   .. py:attribute:: ismap
      :type:  Optional[str]


   .. py:attribute:: loading
      :type:  Optional[str]


   .. py:attribute:: referrer_policy
      :type:  Optional[str]


   .. py:attribute:: sizes
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: srcset
      :type:  Optional[str]


   .. py:attribute:: usemap
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLInputElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: accept
      :type:  Optional[str]


   .. py:attribute:: alt
      :type:  Optional[str]


   .. py:attribute:: auto_complete
      :type:  Optional[str]


   .. py:attribute:: auto_focus
      :type:  Optional[str]


   .. py:attribute:: capture
      :type:  Optional[str]


   .. py:attribute:: checked
      :type:  Optional[str]


   .. py:attribute:: cross_origin
      :type:  Optional[str]


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: form_action
      :type:  Optional[str]


   .. py:attribute:: form_enctype
      :type:  Optional[str]


   .. py:attribute:: form_method
      :type:  Optional[str]


   .. py:attribute:: form_no_validate
      :type:  Optional[str]


   .. py:attribute:: form_target
      :type:  Optional[str]


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: list
      :type:  Optional[str]


   .. py:attribute:: max
      :type:  Optional[str]


   .. py:attribute:: max_length
      :type:  Optional[str]


   .. py:attribute:: min
      :type:  Optional[str]


   .. py:attribute:: min_length
      :type:  Optional[str]


   .. py:attribute:: multiple
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: pattern
      :type:  Optional[str]


   .. py:attribute:: placeholder
      :type:  Optional[str]


   .. py:attribute:: readonly
      :type:  Optional[str]


   .. py:attribute:: required
      :type:  Optional[str]


   .. py:attribute:: selection_direction
      :type:  Optional[str]


   .. py:attribute:: selection_end
      :type:  Optional[str]


   .. py:attribute:: selection_start
      :type:  Optional[str]


   .. py:attribute:: size
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: step
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


   .. py:attribute:: value
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLLabelElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: html_for
      :type:  Optional[str]


.. py:class:: HTMLLegendElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: align
      :type:  Optional[str]


.. py:class:: HTMLLinkElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: html_as
      :type:  Optional[str]


   .. py:attribute:: cross_origin
      :type:  Optional[str]


   .. py:attribute:: disabled
      :type:  Optional[str]


   .. py:attribute:: fetch_priority
      :type:  Optional[Literal['high', 'low', 'auto']]


   .. py:attribute:: href
      :type:  Optional[str]


   .. py:attribute:: hreflang
      :type:  Optional[str]


   .. py:attribute:: image_sizes
      :type:  Optional[str]


   .. py:attribute:: integrity
      :type:  Optional[str]


   .. py:attribute:: media
      :type:  Optional[str]


   .. py:attribute:: referrer_policy
      :type:  Optional[str]


   .. py:attribute:: rel
      :type:  Optional[str]


   .. py:attribute:: sizes
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


.. py:class:: HTMLListItemElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLMapElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: name
      :type:  Optional[str]


.. py:class:: HTMLMeterElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: high
      :type:  Optional[str]


   .. py:attribute:: low
      :type:  Optional[str]


   .. py:attribute:: max
      :type:  Optional[str]


   .. py:attribute:: min
      :type:  Optional[str]


   .. py:attribute:: optimum
      :type:  Optional[str]


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLModElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: cite
      :type:  Optional[str]


   .. py:attribute:: datetime
      :type:  str


.. py:class:: HTMLObjectElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: data
      :type:  Optional[str]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


   .. py:attribute:: usemap
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLOptGroupElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: label
      :type:  Optional[str]


.. py:class:: HTMLOptionElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: label
      :type:  Optional[str]


   .. py:attribute:: selected
      :type:  Optional[str]


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLOrderedListElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: reversed
      :type:  Optional[str]


   .. py:attribute:: start
      :type:  Optional[str]


.. py:class:: HTMLOutputElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: html_for
      :type:  Optional[str]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


.. py:class:: HTMLParagraphElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLParamElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLPictureElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLPragmaMetaElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: http_equiv
      :type:  Optional[str]


.. py:class:: HTMLPreElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLProgressElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: max
      :type:  Optional[str]


   .. py:attribute:: value
      :type:  Optional[str]


.. py:class:: HTMLQuoteElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: cite
      :type:  Optional[str]


.. py:class:: HTMLScriptElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: async_
      :type:  Optional[bool]


   .. py:attribute:: cross_origin
      :type:  Optional[str]


   .. py:attribute:: defer
      :type:  Optional[bool]


   .. py:attribute:: integrity
      :type:  Optional[str]


   .. py:attribute:: nonce
      :type:  Optional[str]


   .. py:attribute:: referrer_policy
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


.. py:class:: HTMLSelectElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: auto_complete
      :type:  Optional[str]


   .. py:attribute:: auto_focus
      :type:  Optional[str]


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: multiple
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: required
      :type:  Optional[str]


   .. py:attribute:: size
      :type:  Optional[str]


.. py:class:: HTMLSlotElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: name
      :type:  Optional[str]


.. py:class:: HTMLSourceElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: media
      :type:  Optional[str]


   .. py:attribute:: sizes
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: srcset
      :type:  Optional[str]


   .. py:attribute:: type
      :type:  Optional[str]


.. py:class:: HTMLSpanElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLStyleElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: media
      :type:  Optional[str]


   .. py:attribute:: nonce
      :type:  Optional[str]


   .. py:attribute:: scoped
      :type:  Optional[str]


.. py:class:: HTMLTableCaptionElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLTableCellElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: abbr
      :type:  Optional[str]


   .. py:attribute:: colspan
      :type:  Optional[str]


   .. py:attribute:: headers
      :type:  Optional[str]


   .. py:attribute:: rowspan
      :type:  Optional[str]


   .. py:attribute:: scope
      :type:  Optional[str]


.. py:class:: HTMLTableColElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: span
      :type:  Optional[str]


.. py:class:: HTMLTableDataCellElement

   Bases: :py:obj:`pydom.types.html.html_table_cell_element.HTMLTableCellElement`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLTableElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: border
      :type:  Optional[str]


   .. py:attribute:: cellpadding
      :type:  Optional[str]


   .. py:attribute:: cellspacing
      :type:  Optional[str]


   .. py:attribute:: frame
      :type:  Optional[str]


   .. py:attribute:: rules
      :type:  Optional[str]


   .. py:attribute:: summary
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:class:: HTMLTableHeaderCellElement

   Bases: :py:obj:`pydom.types.html.html_table_cell_element.HTMLTableCellElement`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLTableRowElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: align
      :type:  Optional[str]


   .. py:attribute:: bgcolor
      :type:  Optional[str]


   .. py:attribute:: ch
      :type:  Optional[str]


   .. py:attribute:: choff
      :type:  Optional[str]


   .. py:attribute:: v_align
      :type:  Optional[str]


.. py:class:: HTMLTableSectionElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: align
      :type:  Optional[str]


   .. py:attribute:: ch
      :type:  Optional[str]


   .. py:attribute:: choff
      :type:  Optional[str]


   .. py:attribute:: v_align
      :type:  Optional[str]


.. py:class:: HTMLTemplateElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLTextAreaElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: auto_complete
      :type:  Optional[str]


   .. py:attribute:: auto_focus
      :type:  Optional[str]


   .. py:attribute:: cols
      :type:  Optional[str]


   .. py:attribute:: dirname
      :type:  Optional[str]


   .. py:attribute:: disabled
      :type:  Optional[bool]


   .. py:attribute:: form
      :type:  Optional[str]


   .. py:attribute:: max_length
      :type:  Optional[str]


   .. py:attribute:: min_length
      :type:  Optional[str]


   .. py:attribute:: name
      :type:  Optional[str]


   .. py:attribute:: placeholder
      :type:  Optional[str]


   .. py:attribute:: readonly
      :type:  Optional[str]


   .. py:attribute:: required
      :type:  Optional[str]


   .. py:attribute:: rows
      :type:  Optional[str]


   .. py:attribute:: wrap
      :type:  Optional[str]


.. py:class:: HTMLTimeElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: datetime
      :type:  Optional[str]


.. py:class:: HTMLTitleElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLTrackElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: default
      :type:  Optional[str]


   .. py:attribute:: kind
      :type:  Optional[str]


   .. py:attribute:: label
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: srclang
      :type:  Optional[str]


.. py:class:: HTMLUnorderedListElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


.. py:class:: HTMLUserMetaElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: itemprop
      :type:  Optional[str]


.. py:class:: HTMLVideoElement

   Bases: :py:obj:`pydom.types.html.html_element_props.HTMLElementProps`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: auto_play
      :type:  Optional[str]


   .. py:attribute:: controls
      :type:  Optional[str]


   .. py:attribute:: cross_origin
      :type:  Optional[str]


   .. py:attribute:: height
      :type:  Optional[str]


   .. py:attribute:: loop
      :type:  Optional[str]


   .. py:attribute:: muted
      :type:  Optional[str]


   .. py:attribute:: plays_inline
      :type:  Optional[str]


   .. py:attribute:: poster
      :type:  Optional[str]


   .. py:attribute:: preload
      :type:  Optional[str]


   .. py:attribute:: src
      :type:  Optional[str]


   .. py:attribute:: width
      :type:  Optional[str]


.. py:data:: ChildType
   :type:  typing_extensions.TypeAlias

.. py:data:: ChildrenType
   :type:  typing_extensions.TypeAlias

.. py:data:: Primitive
   :type:  typing_extensions.TypeAlias

.. py:data:: Renderable
   :type:  typing_extensions.TypeAlias

.. py:data:: RenderResult
   :type:  typing_extensions.TypeAlias

.. py:data:: RenderTarget
   :type:  typing_extensions.TypeAlias

.. py:class:: RenderResultJSON

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: type
      :type:  str


   .. py:attribute:: props
      :type:  Dict[str, Primitive]


   .. py:attribute:: children
      :type:  List[RenderResultJSON]


.. py:class:: CSSProperties

   Bases: :py:obj:`typing_extensions.TypedDict`


   dict() -> new empty dictionary
   dict(mapping) -> new dictionary initialized from a mapping object's
       (key, value) pairs
   dict(iterable) -> new dictionary initialized as if via:
       d = {}
       for k, v in iterable:
           d[k] = v
   dict(**kwargs) -> new dictionary initialized with the name=value pairs
       in the keyword argument list.  For example:  dict(one=1, two=2)


   .. py:attribute:: align_content
      :type:  AlignContent


   .. py:attribute:: align_items
      :type:  Literal['flex-start', 'flex-end', 'center', 'baseline', 'stretch']


   .. py:attribute:: align_self
      :type:  Union[str, Literal['auto', 'flex-start', 'flex-end', 'center', 'baseline', 'stretch']]


   .. py:attribute:: animation
      :type:  str


   .. py:attribute:: animation_delay
      :type:  str


   .. py:attribute:: animation_direction
      :type:  Union[str, Literal['normal', 'reverse', 'alternate', 'alternate-reverse']]


   .. py:attribute:: animation_duration
      :type:  str


   .. py:attribute:: animation_fill_mode
      :type:  Union[str, Literal['none', 'forwards', 'backwards', 'both']]


   .. py:attribute:: animation_iteration_count
      :type:  Union[str, Literal['infinite', 'n']]


   .. py:attribute:: animation_name
      :type:  str


   .. py:attribute:: animation_play_state
      :type:  Union[str, Literal['running', 'paused']]


   .. py:attribute:: animation_timing_function
      :type:  str


   .. py:attribute:: backface_visibility
      :type:  Union[str, Literal['visible', 'hidden']]


   .. py:attribute:: background
      :type:  str


   .. py:attribute:: background_attachment
      :type:  Union[str, Literal['scroll', 'fixed', 'local']]


   .. py:attribute:: background_blend_mode
      :type:  str


   .. py:attribute:: background_clip
      :type:  Union[str, Literal['border-box', 'padding-box', 'content-box']]


   .. py:attribute:: background_color
      :type:  str


   .. py:attribute:: background_image
      :type:  str


   .. py:attribute:: background_origin
      :type:  Union[str, Literal['padding-box', 'border-box', 'content-box']]


   .. py:attribute:: background_position
      :type:  str


   .. py:attribute:: background_repeat
      :type:  Union[str, Literal['repeat', 'repeat-x', 'repeat-y', 'no-repeat', 'space', 'round']]


   .. py:attribute:: background_size
      :type:  str


   .. py:attribute:: border
      :type:  str


   .. py:attribute:: border_bottom
      :type:  str


   .. py:attribute:: border_bottom_color
      :type:  str


   .. py:attribute:: border_bottom_left_radius
      :type:  str


   .. py:attribute:: border_bottom_right_radius
      :type:  str


   .. py:attribute:: border_bottom_style
      :type:  str


   .. py:attribute:: border_bottom_width
      :type:  str


   .. py:attribute:: border_collapse
      :type:  Union[str, Literal['collapse', 'separate']]


   .. py:attribute:: border_color
      :type:  str


   .. py:attribute:: border_image
      :type:  str


   .. py:attribute:: border_image_outset
      :type:  str


   .. py:attribute:: border_image_repeat
      :type:  Union[str, Literal['stretch', 'repeat', 'round']]


   .. py:attribute:: border_image_slice
      :type:  str


   .. py:attribute:: border_image_source
      :type:  str


   .. py:attribute:: border_image_width
      :type:  str


   .. py:attribute:: border_left
      :type:  str


   .. py:attribute:: border_left_color
      :type:  str


   .. py:attribute:: border_left_style
      :type:  str


   .. py:attribute:: border_left_width
      :type:  str


   .. py:attribute:: border_radius
      :type:  str


   .. py:attribute:: border_right
      :type:  str


   .. py:attribute:: border_right_color
      :type:  str


   .. py:attribute:: border_right_style
      :type:  str


   .. py:attribute:: border_right_width
      :type:  str


   .. py:attribute:: border_spacing
      :type:  str


   .. py:attribute:: border_style
      :type:  str


   .. py:attribute:: border_top
      :type:  str


   .. py:attribute:: border_top_color
      :type:  str


   .. py:attribute:: border_top_left_radius
      :type:  str


   .. py:attribute:: border_top_right_radius
      :type:  str


   .. py:attribute:: border_top_style
      :type:  str


   .. py:attribute:: border_top_width
      :type:  str


   .. py:attribute:: border_width
      :type:  str


   .. py:attribute:: bottom
      :type:  str


   .. py:attribute:: box_shadow
      :type:  str


   .. py:attribute:: box_sizing
      :type:  Union[str, Literal['content-box', 'border-box']]


   .. py:attribute:: caption_side
      :type:  Union[str, Literal['top', 'bottom']]


   .. py:attribute:: clear
      :type:  Union[str, Literal['none', 'left', 'right', 'both']]

      D.clear() -> None.  Remove all items from D.



   .. py:attribute:: clip
      :type:  str


   .. py:attribute:: color
      :type:  str


   .. py:attribute:: column_count
      :type:  Union[str, int]


   .. py:attribute:: column_fill
      :type:  Union[str, Literal['balance', 'auto']]


   .. py:attribute:: column_gap
      :type:  str


   .. py:attribute:: column_rule
      :type:  str


   .. py:attribute:: column_rule_color
      :type:  str


   .. py:attribute:: column_rule_style
      :type:  str


   .. py:attribute:: column_rule_width
      :type:  str


   .. py:attribute:: column_span
      :type:  Union[str, Literal['none', 'all']]


   .. py:attribute:: column_width
      :type:  Union[str, int]


   .. py:attribute:: columns
      :type:  str


   .. py:attribute:: content
      :type:  str


   .. py:attribute:: counter_increment
      :type:  str


   .. py:attribute:: counter_reset
      :type:  str


   .. py:attribute:: cursor
      :type:  str


   .. py:attribute:: direction
      :type:  Union[str, Literal['ltr', 'rtl']]


   .. py:attribute:: display
      :type:  Union[str, Literal['block', 'inline', 'inline-block', 'flex', 'inline-flex', 'grid', 'inline-grid', 'table', 'table-row', 'table-cell', 'none']]


   .. py:attribute:: empty_cells
      :type:  Union[str, Literal['show', 'hide']]


   .. py:attribute:: filter
      :type:  str


   .. py:attribute:: flex
      :type:  str


   .. py:attribute:: flex_basis
      :type:  str


   .. py:attribute:: flex_direction
      :type:  Union[str, Literal['row', 'row-reverse', 'column', 'column-reverse']]


   .. py:attribute:: flex_flow
      :type:  str


   .. py:attribute:: flex_grow
      :type:  str


   .. py:attribute:: flex_shrink
      :type:  str


   .. py:attribute:: flex_wrap
      :type:  Union[str, Literal['nowrap', 'wrap', 'wrap-reverse']]


   .. py:attribute:: float
      :type:  Union[str, Literal['left', 'right', 'none']]


   .. py:attribute:: font
      :type:  str


   .. py:attribute:: font_family
      :type:  str


   .. py:attribute:: font_feature_settings
      :type:  str


   .. py:attribute:: font_kerning
      :type:  Union[str, Literal['auto', 'normal', 'none']]


   .. py:attribute:: font_language_override
      :type:  str


   .. py:attribute:: font_size
      :type:  str


   .. py:attribute:: font_size_adjust
      :type:  Union[str, Literal['none']]


   .. py:attribute:: font_stretch
      :type:  str


   .. py:attribute:: font_style
      :type:  Union[str, Literal['normal', 'italic', 'oblique']]


   .. py:attribute:: font_synthesis
      :type:  str


   .. py:attribute:: font_variant
      :type:  str


   .. py:attribute:: font_variant_alternates
      :type:  str


   .. py:attribute:: font_variant_caps
      :type:  Union[str, Literal['normal', 'small-caps']]


   .. py:attribute:: font_variant_east_asian
      :type:  str


   .. py:attribute:: font_variant_ligatures
      :type:  str


   .. py:attribute:: font_variant_numeric
      :type:  str


   .. py:attribute:: font_variant_position
      :type:  Union[str, Literal['normal', 'sub', 'super']]


   .. py:attribute:: font_weight
      :type:  Union[str, Literal['normal', 'bold', 'bolder', 'lighter', '100', '200', '300', '400', '500', '600', '700', '800', '900']]


   .. py:attribute:: grid
      :type:  str


   .. py:attribute:: grid_area
      :type:  str


   .. py:attribute:: grid_auto_columns
      :type:  str


   .. py:attribute:: grid_auto_flow
      :type:  str


   .. py:attribute:: grid_auto_rows
      :type:  str


   .. py:attribute:: grid_column
      :type:  str


   .. py:attribute:: grid_column_end
      :type:  str


   .. py:attribute:: grid_column_gap
      :type:  str


   .. py:attribute:: grid_column_start
      :type:  str


   .. py:attribute:: grid_gap
      :type:  str


   .. py:attribute:: grid_row
      :type:  str


   .. py:attribute:: grid_row_end
      :type:  str


   .. py:attribute:: grid_row_gap
      :type:  str


   .. py:attribute:: grid_row_start
      :type:  str


   .. py:attribute:: grid_template
      :type:  str


   .. py:attribute:: grid_template_areas
      :type:  str


   .. py:attribute:: grid_template_columns
      :type:  str


   .. py:attribute:: grid_template_rows
      :type:  str


   .. py:attribute:: height
      :type:  str


   .. py:attribute:: hyphens
      :type:  Union[str, Literal['none', 'manual', 'auto']]


   .. py:attribute:: image_rendering
      :type:  str


   .. py:attribute:: isolation
      :type:  Union[str, Literal['auto', 'isolate']]


   .. py:attribute:: justify_content
      :type:  Union[str, Literal['flex-start', 'flex-end', 'center', 'space-between', 'space-around', 'space-evenly']]


   .. py:attribute:: left
      :type:  str


   .. py:attribute:: letter_spacing
      :type:  str


   .. py:attribute:: line_break
      :type:  Union[str, Literal['auto', 'loose', 'normal', 'strict']]


   .. py:attribute:: line_height
      :type:  Union[str, int]


   .. py:attribute:: list_style
      :type:  str


   .. py:attribute:: list_style_image
      :type:  str


   .. py:attribute:: list_style_position
      :type:  Union[str, Literal['inside', 'outside']]


   .. py:attribute:: list_style_type
      :type:  str


   .. py:attribute:: margin
      :type:  str


   .. py:attribute:: margin_bottom
      :type:  str


   .. py:attribute:: margin_left
      :type:  str


   .. py:attribute:: margin_right
      :type:  str


   .. py:attribute:: margin_top
      :type:  str


   .. py:attribute:: max_height
      :type:  str


   .. py:attribute:: max_width
      :type:  str


   .. py:attribute:: min_height
      :type:  str


   .. py:attribute:: min_width
      :type:  str


   .. py:attribute:: mix_blend_mode
      :type:  str


   .. py:attribute:: object_fit
      :type:  Union[str, Literal['fill', 'contain', 'cover', 'none', 'scale-down']]


   .. py:attribute:: object_position
      :type:  str


   .. py:attribute:: opacity
      :type:  Union[str, float_]


   .. py:attribute:: order
      :type:  Union[str, int]


   .. py:attribute:: outline
      :type:  str


   .. py:attribute:: outline_color
      :type:  str


   .. py:attribute:: outline_offset
      :type:  str


   .. py:attribute:: outline_style
      :type:  str


   .. py:attribute:: outline_width
      :type:  str


   .. py:attribute:: overflow
      :type:  Union[str, Literal['auto', 'hidden', 'scroll', 'visible']]


   .. py:attribute:: overflow_wrap
      :type:  Union[str, Literal['normal', 'break-word', 'anywhere']]


   .. py:attribute:: overflow_x
      :type:  Union[str, Literal['auto', 'hidden', 'scroll', 'visible']]


   .. py:attribute:: overflow_y
      :type:  Union[str, Literal['auto', 'hidden', 'scroll', 'visible']]


   .. py:attribute:: padding
      :type:  str


   .. py:attribute:: padding_bottom
      :type:  str


   .. py:attribute:: padding_left
      :type:  str


   .. py:attribute:: padding_right
      :type:  str


   .. py:attribute:: padding_top
      :type:  str


   .. py:attribute:: page_break_after
      :type:  Union[str, Literal['auto', 'always', 'avoid', 'left', 'right']]


   .. py:attribute:: page_break_before
      :type:  Union[str, Literal['auto', 'always', 'avoid', 'left', 'right']]


   .. py:attribute:: page_break_inside
      :type:  Union[str, Literal['auto', 'avoid']]


   .. py:attribute:: perspective
      :type:  str


   .. py:attribute:: perspective_origin
      :type:  str


   .. py:attribute:: position
      :type:  Union[str, Literal['static', 'relative', 'absolute', 'fixed', 'sticky']]


   .. py:attribute:: quotes
      :type:  str


   .. py:attribute:: resize
      :type:  Union[str, Literal['none', 'both', 'horizontal', 'vertical']]


   .. py:attribute:: right
      :type:  str


   .. py:attribute:: scroll_behavior
      :type:  Union[str, Literal['auto', 'smooth']]


   .. py:attribute:: tab_size
      :type:  Union[str, int]


   .. py:attribute:: table_layout
      :type:  Union[str, Literal['auto', 'fixed']]


   .. py:attribute:: text_align
      :type:  Union[str, Literal['left', 'right', 'center', 'justify', 'start', 'end']]


   .. py:attribute:: text_align_last
      :type:  Union[str, Literal['auto', 'left', 'right', 'center', 'justify', 'start', 'end']]


   .. py:attribute:: text_decoration
      :type:  str


   .. py:attribute:: text_decoration_color
      :type:  str


   .. py:attribute:: text_decoration_line
      :type:  str


   .. py:attribute:: text_decoration_style
      :type:  str


   .. py:attribute:: text_indent
      :type:  str


   .. py:attribute:: text_justify
      :type:  Union[str, Literal['auto', 'inter-word', 'inter-character', 'none']]


   .. py:attribute:: text_overflow
      :type:  Union[str, Literal['clip', 'ellipsis']]


   .. py:attribute:: text_shadow
      :type:  str


   .. py:attribute:: text_transform
      :type:  Union[str, Literal['none', 'capitalize', 'uppercase', 'lowercase', 'full-width']]


   .. py:attribute:: text_underline_position
      :type:  str


   .. py:attribute:: top
      :type:  str


   .. py:attribute:: transform
      :type:  str


   .. py:attribute:: transform_origin
      :type:  str


   .. py:attribute:: transform_style
      :type:  Union[str, Literal['flat', 'preserve-3d']]


   .. py:attribute:: transition
      :type:  str


   .. py:attribute:: transition_delay
      :type:  str


   .. py:attribute:: transition_duration
      :type:  str


   .. py:attribute:: transition_property
      :type:  str


   .. py:attribute:: transition_timing_function
      :type:  str


   .. py:attribute:: unicode_bidi
      :type:  Union[str, Literal['normal', 'embed', 'isolate', 'bidi-override']]


   .. py:attribute:: user_select
      :type:  Union[str, Literal['auto', 'text', 'none', 'contain', 'all']]


   .. py:attribute:: vertical_align
      :type:  str


   .. py:attribute:: visibility
      :type:  Union[str, Literal['visible', 'hidden', 'collapse']]


   .. py:attribute:: white_space
      :type:  Union[str, Literal['normal', 'nowrap', 'pre', 'pre-line', 'pre-wrap']]


   .. py:attribute:: widows
      :type:  Union[str, int]


   .. py:attribute:: width
      :type:  str


   .. py:attribute:: will_change
      :type:  str


   .. py:attribute:: word_break
      :type:  Union[str, Literal['normal', 'break-all', 'keep-all', 'break-word']]


   .. py:attribute:: word_spacing
      :type:  str


   .. py:attribute:: writing_mode
      :type:  Union[str, Literal['horizontal-tb', 'vertical-rl', 'vertical-lr', 'sideways-rl', 'sideways-lr']]


   .. py:attribute:: z_index
      :type:  Union[str, int]


