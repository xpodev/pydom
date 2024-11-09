from ...transformers import PropertyTransformer

_SIMPLE_TRANSFORMERS = {
    "html_for": "for",
    "accept_charset": "accept-charset",
    "http_equiv": "http-equiv",
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

    def transform(self, prop_name, _, element):
        element.props[_SIMPLE_TRANSFORMERS[prop_name]] = _
        del element.props[prop_name]
