from ....rendering.transformers import PropertyTransformer


class ClassTransformer(PropertyTransformer):
    def __init__(self, prop_name="classes"):
        self.prop_name = prop_name

    def match(self, prop_name, _) -> bool:
        return prop_name == self.prop_name

    def transform(self, _, prop_value, element):
        if not isinstance(prop_value, str):
            prop_value = " ".join(prop_value)

        element.props["class"] = " ".join(str(prop_value).split()).strip()
        del element.props[self.prop_name]
