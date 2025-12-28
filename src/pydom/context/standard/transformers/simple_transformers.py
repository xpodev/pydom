from ....rendering.transformers import PropertyTransformer

_SIMPLE_TRANSFORMERS = {
    "html_for": "for",
    "access_key": "accesskey",
    "content_editable": "contenteditable",
    "cross_origin": "crossorigin",
    "tab_index": "tabindex",
    "use_map": "usemap",
    "col_span": "colspan",
    "row_span": "rowspan",
    "char_set": "charset",
}


class SimpleTransformer(PropertyTransformer):
    def match(self, prop_name, _) -> bool:
        return prop_name in _SIMPLE_TRANSFORMERS

    def transform(self, prop_name, prop_value, element, /):
        element.props[_SIMPLE_TRANSFORMERS[prop_name]] = prop_value
        del element.props[prop_name]


_SIMPLE_INPUT_TRANSFORMERS = {
    "auto_capitalize": "autocapitalize",
    "auto_complete": "autocomplete",
    "auto_focus": "autofocus",
    "form_action": "formaction",
    "form_enctype": "formenctype",
    "form_method": "formmethod",
    "form_no_validate": "formnovalidate",
    "form_target": "formtarget",
    "max_length": "maxlength",
    "min_length": "minlength",
    "popover_target": "popovertarget",
    "popover_target_action": "popovertargetaction",
}


class SimpleInputTransformer(PropertyTransformer):
    def match(self, prop_name, _) -> bool:
        return prop_name in _SIMPLE_INPUT_TRANSFORMERS

    def transform(self, prop_name, prop_value, element, /):
        if element.node.tag_name != "input":
            return
        element.props[_SIMPLE_INPUT_TRANSFORMERS[prop_name]] = prop_value
        del element.props[prop_name]
