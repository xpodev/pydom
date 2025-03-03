import typing_extensions as t

from pydom.context.context import Context, PropertyTransformer
from pydom.html import Script, Style
from pydom.types.html import HTMLScriptElement

T = t.TypeVar("T")


class HTMXTransformer(PropertyTransformer):
    NORMAL_KEYS = {
        "hx_get": "hx-get",
        "hx_post": "hx-post",
        "hx_push_url": "hx-push-url",
        "hx_select": "hx-select",
        "hx_select_oob": "hx-select-oob",
        "hx_swap": "hx-swap",
        "hx_swap_oob": "hx-swap-oob",
        "hx_target": "hx-target",
        "hx_trigger": "hx-trigger",
        "hx_vals": "hx-vals",
        "hx_boost": "hx-boost",
        "hx_confirm": "hx-confirm",
        "hx_delete": "hx-delete",
        "hx_disable": "hx-disable",
        "hx_disabled_elt": "hx-disabled-elt",
        "hx_disinherit": "hx-disinherit",
        "hx_encoding": "hx-encoding",
        "hx_ext": "hx-ext",
        "hx_headers": "hx-headers",
        "hx_history": "hx-history",
        "hx_history_elt": "hx-history-elt",
        "hx_include": "hx-include",
        "hx_indicator": "hx-indicator",
        "hx_inherit": "hx-inherit",
        "hx_params": "hx-params",
        "hx_patch": "hx-patch",
        "hx_preserve": "hx-preserve",
        "hx_prompt": "hx-prompt",
        "hx_put": "hx-put",
        "hx_replace_url": "hx-replace-url",
        "hx_request": "hx-request",
        "hx_sync": "hx-sync",
        "hx_validate": "hx-validate",
        "hx_vars": "hx-vars",
    }

    def match(self, key: str, value):
        return key.startswith("hx_")

    def transform(self, key: str, value, element):
        if key in self.NORMAL_KEYS:
            element.props[self.NORMAL_KEYS[key]] = value
            del element.props[key]

        # hx-on:*
        elif key.startswith("hx_on_"):
            if key.startswith("hx_on_htmx_"):
                # Special case for htmx events: hx-on:htmx:*
                prefix = "hx-on:htmx:"
                event = key.removeprefix("hx_on_htmx_")

            elif key.startswith("hx_on__"):
                # Special case for htmx events: hx-on::*
                prefix = "hx-on::"
                event = key.removeprefix("hx_on__")

            else:  # key.startswith("hx_on_")
                # regular events: hx-on:*
                prefix = "hx-on:"
                event = key.removeprefix("hx_on_")

            if "__" in event:
                # some events uses : as a separator, in python we use __ to indicate that
                event = event.replace("__", ":")

            event = event.replace("_", "-")

            new_key = f"{prefix}{event}"

            element.props[new_key] = value
            del element.props[key]


def setup_htmx_transformers(
    ctx: Context,
    extensions: t.Sequence["HTMXExtension"] = (),
) -> Context:
    from pydom.context.standard.transformers.html_events_transformer import (
        HTMLEventsTransformer,
    )

    ctx.add_prop_transformer(
        HTMXTransformer(),
        before=[HTMLEventsTransformer],
    )

    for extension in extensions:
        transformer = extension.transformer()
        ctx.add_prop_transformer(transformer, before=[HTMXTransformer])

    return ctx


class PartialScript(Script):
    def __init__(self, *children: str, **kwargs: t.Unpack["HTMLScriptElement"]):
        super().__init__(*children, **kwargs)

    def __call__(self, **more: t.Unpack[HTMLScriptElement]) -> Script:
        props_not_in_self: dict = {k: v for k, v in more.items() if k not in self.props}
        final_props = {**self.props, **props_not_in_self}
        return Script(**final_props)


class HTMX:
    def __init__(self, version="2.0.2"):
        self.script = PartialScript(
            src=f"https://unpkg.com/htmx.org@{version}",
            integrity="sha384-Y7hw+L/jvKeWIRRkqWYfPcvVxHzVzn5REgzbawhxAuQGwX1XWe70vji+VSeHOThJ",
            cross_origin="anonymous",
        )
        self.unminified_script = PartialScript(
            src=f"https://unpkg.com/htmx.org@{version}/dist/htmx.js",
            integrity="sha384-yZq+5izaUBKcRgFbxgkRYwpHhHHCpp5nseXp0MEQ1A4MTWVMnqkmcuFez8x5qfxr",
            cross_origin="anonymous",
        )


class HTMXExtension(t.Protocol):
    name: str
    script: PartialScript
    mapping: t.Dict[str, str]
    link: t.Optional[str] = None

    def transformer(self) -> PropertyTransformer:
        class Transformer(PropertyTransformer):
            def __init__(self, mapping):
                self.mapping = mapping

            def match(self, key, _):
                return key in self.mapping

            def transform(self, key, value, element):
                element.props[self.mapping[key]] = value
                del element.props[key]

        return Transformer(self.mapping)

    def render(self):
        yield self.script()


###############################################
# HTMX Extensions
###############################################


class HTMXSSEExtension(HTMXExtension):
    name = "sse"
    link = "https://github.com/bigskysoftware/htmx-extensions/tree/main/src/sse"
    mapping = {
        "sse_connect": "hx-sse-connect",
        "sse_swap": "hx-sse-swap",
        "sse_close": "hx-sse-close",
    }

    def __init__(self, version="2.2.2"):
        self.script = PartialScript(
            src=f"https://unpkg.com/htmx-ext-sse@{version}/sse.js"
        )


class HTMXJsonEncExtension(HTMXExtension):
    name = "json-enc"
    link = "https://github.com/bigskysoftware/htmx-extensions/tree/main/src/json-enc"
    mapping = {}

    def __init__(self, version="2.0.1"):
        self.script = PartialScript(
            src=f"https://unpkg.com/htmx-ext-json-enc@{version}/json-enc.js"
        )


class HTMXMultiSwapExtension(HTMXExtension):
    name = "multi-swap"
    link = "https://github.com/bigskysoftware/htmx-extensions/blob/main/src/multi-swap/README.md"
    mapping = {}

    def __init__(self, version="2.0.0"):
        self.script = PartialScript(
            src=f"https://unpkg.com/htmx-ext-multi-swap@{version}/multi-swap.js"
        )


class HTMXLoadingStatesExtension(HTMXExtension):
    name = "loading-states"
    link = (
        "https://github.com/bigskysoftware/htmx-extensions/tree/main/src/loading-states"
    )
    mapping = {}

    def __init__(self, version="2.0.0"):
        self.script = PartialScript(
            src=f"https://unpkg.com/htmx-ext-loading-states@{version}/loading-states.js"
        )
        self.style = Style("[data-loading] { display: none; }")

    def render(self):
        yield from super().render()
        yield self.style()


class HTMXClassToolsExtension(HTMXExtension):
    name = "class-tools"
    link = "https://github.com/bigskysoftware/htmx-extensions/tree/main/src/class-tools"
    mapping = {
        'hx_classes': 'classes',
        'data_classes': 'data-classes',
        'apply_parent_classes': 'apply-parent-classes',
        'data_apply_parent_classes': 'data-apply-parent-classes',
    }

    def __init__(self, version="2.0.1"):
        self.script = PartialScript(
            src=f"https://unpkg.com/htmx-ext-class-tools@{version}/class-tools.js"
        )
