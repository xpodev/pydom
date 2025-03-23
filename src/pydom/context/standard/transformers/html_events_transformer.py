from ....rendering.transformers import PropertyTransformer


class HTMLEventsTransformer(PropertyTransformer):
    def match(self, prop_name, prop_value) -> bool:
        return prop_name.startswith("on_") and isinstance(prop_value, str)

    def transform(self, prop_name, prop_value, element):
        event_name = prop_name.replace("_", "").lower()
        element.props[event_name] = prop_value
        del element.props[prop_name]
