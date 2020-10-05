from typing import Any

from instant_eda.report.presentation.core.item_renderer import ItemRenderer
from instant_eda.report.presentation.core.renderable import Renderable
from instant_eda.report.presentation.core.toggle_button import ToggleButton


class Collapse(ItemRenderer):
    def __init__(self, button: ToggleButton, item: Renderable, **kwargs):
        super().__init__("collapse", {"button": button, "item": item}, **kwargs)

    def __repr__(self):
        return "Collapse"

    def render(self) -> Any:
        raise NotImplementedError()

    @classmethod
    def convert_to_class(cls, obj, flv):
        obj.__class__ = cls
        if "button" in obj.content:
            flv(obj.content["button"])
        if "item" in obj.content:
            flv(obj.content["item"])
