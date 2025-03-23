from ....rendering.transformers import PropertyTransformer
from ....utils.functions import is_primitive


class DashTransformer(PropertyTransformer):
    def match(self, prop_name, _) -> bool:
        return "_" in prop_name and is_primitive(_)

    def transform(self, _, prop_value, element):
        dash_key = _.replace("_", "-")
        element.props[dash_key] = prop_value
        del element.props[_]
