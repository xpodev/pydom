import re

from os import PathLike
from pathlib import Path
from typing import Union, Dict

import cssutils

from ..utils.get_frame import get_frame

from ..utils.functions import random_string, remove_prefix


class CSSClass:
    def __init__(self, class_name: str):
        self.class_name = class_name
        self.sub_rules: Dict[str, Dict[str, str]] = {}
        self.uuid = random_string()

    def add_rule(self, rule: str, properties: Dict[str, str]):
        self.sub_rules.setdefault(rule, {}).update(properties)

    def to_css_string(self, minified=False):
        rules = []
        rules_format_string = (
            ".{0}{1} {{\n{2}}}\n" if not minified else ".{0}{1}{{{2}}}"
        )
        single_rule_format_string = "\t{0}: {1}\n" if not minified else "{0}:{1}"
        for key, rule in self.sub_rules.items():
            rule_text = ""
            for attr, value in rule.items():
                value = value.strip()
                if not value.endswith(";"):
                    value += ";"
                rule_text += single_rule_format_string.format(attr, value)

            rules.append(rules_format_string.format(self.uuid, key, rule_text))

        join_string = "" if minified else "\n"
        return join_string.join(rules)

    def __str__(self):
        return self.uuid


class CSSModule:
    def __init__(self, module_name):
        css = cssutils.parseFile(module_name)
        self.module_name = module_name
        self.classes: Dict[str, CSSClass] = {}
        self.raw_css = ""
        for rule in css:
            if rule.type == rule.STYLE_RULE:
                selectors = rule.selectorList
                first_selector = selectors[0]

                # if the first selector starts with @ add it to the global styles
                if first_selector.seq[0].type == "at-keyword":
                    continue

                if first_selector.seq[0].type != "class":
                    continue

                style_dict = {
                    css_property.name: css_property.value for css_property in rule.style
                }

                base_name = remove_prefix(first_selector.seq[0].value, ".")
                css_class = self.classes.get(base_name, CSSClass(base_name))
                for selector in selectors:
                    css_class.add_rule(
                        selector.selectorText.replace(f".{base_name}", ""), style_dict
                    )

                self.classes[base_name] = css_class

            if rule.type == rule.UNKNOWN_RULE:
                self.raw_css += rule.cssText

    def __getattr__(self, __name: str) -> str:
        if __name not in self.classes:
            raise AttributeError(f"CSS class {__name} not found in {self.module_name}")
        return self.classes[__name].uuid

    def to_css_string(self, minified=False):
        raw_css = (
            self.raw_css.replace("\n", "").replace("\t", "")
            if minified
            else self.raw_css
        )
        raw_css = re.sub(r"\s+", " ", raw_css) if minified else raw_css
        join_string = "" if minified else "\n\n"
        return join_string.join(
            [
                *(
                    css_class.to_css_string(minified)
                    for css_class in self.classes.values()
                ),
                raw_css,
            ]
        )


class CSSModulesManager(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls.modules: Dict[str, CSSModule] = {}
        cls.folder: Path = Path.cwd()

    def module(cls, css_path: Union[PathLike, str]):
        """
        Get a CSS module by its path.
        This will return a CSSModule object.
        """
        css_path = str(cls._full_path(css_path).resolve())
        if css_path not in cls.modules:
            cls.modules[css_path] = CSSModule(css_path)
        return cls.modules[css_path]

    def to_css_string(cls, minified=False):
        """
        Get the CSS output of all the CSS modules.
        """
        join_string = "" if minified else "\n\n"
        return join_string.join(
            css_module.to_css_string(minified) for css_module in cls.modules.values()
        )

    def set_root_folder(cls, folder: Union[PathLike, str]):
        """
        Set the folder where the CSS files are located.
        """
        folder = Path(folder)

        cls.folder = folder.absolute()

    def _full_path(cls, css_path: Union[PathLike, str]) -> Path:
        if isinstance(css_path, str):
            if css_path.startswith("./") or css_path.startswith("../"):
                frame = get_frame(2)
                module = frame.f_globals["__file__"]
                css_path = Path(module).parent / css_path

        css_path = Path(css_path)

        if not css_path.is_absolute():
            return cls.folder / css_path

        return css_path


class CSS(metaclass=CSSModulesManager):
    pass


__all__ = ["CSS"]
