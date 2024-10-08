from typing import Optional
from typing_extensions import TypedDict


class AriaProps(TypedDict, total=False):
    aria_active_descendant: Optional[str]
    aria_atomic: Optional[str]
    aria_auto_complete: Optional[str]
    aria_busy: Optional[str]
    aria_checked: Optional[str]
    aria_col_count: Optional[str]
    aria_col_index: Optional[str]
    aria_col_span: Optional[str]
    aria_controls: Optional[str]
    aria_current: Optional[str]
    aria_described_by: Optional[str]
    aria_details: Optional[str]
    aria_disabled: Optional[str]
    aria_drop_effect: Optional[str]
    aria_error_message: Optional[str]
    aria_expanded: Optional[str]
    aria_flow_to: Optional[str]
    aria_grabbed: Optional[str]
    aria_has_popup: Optional[str]
    aria_hidden: Optional[str]
    aria_invalid: Optional[str]
    aria_key_shortcuts: Optional[str]
    aria_label: Optional[str]
    aria_labelled_by: Optional[str]
    aria_level: Optional[str]
    aria_live: Optional[str]
    aria_modal: Optional[str]
    aria_multiline: Optional[str]
    aria_multi_selectable: Optional[str]
    aria_orientation: Optional[str]
    aria_owns: Optional[str]
    aria_placeholder: Optional[str]
    aria_pos_inset: Optional[str]
    aria_pressed: Optional[str]
    aria_readonly: Optional[str]
    aria_relevant: Optional[str]
    aria_required: Optional[str]
    aria_role_description: Optional[str]
    aria_row_count: Optional[str]
    aria_row_index: Optional[str]
    aria_row_span: Optional[str]
    aria_selected: Optional[str]
    aria_set_size: Optional[str]
    aria_sort: Optional[str]
    aria_value_max: Optional[str]
    aria_value_min: Optional[str]
    aria_value_now: Optional[str]
    aria_value_text: Optional[str]
