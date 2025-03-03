pydom.types.styling.css_properties
==================================

.. py:module:: pydom.types.styling.css_properties


Classes
-------

.. autoapisummary::

   pydom.types.styling.css_properties.CSSProperties


Module Contents
---------------

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


