from typing import Any

from instant_eda.report.presentation.core.item_renderer import ItemRenderer


class Table(ItemRenderer):
    def __init__(self, rows, name=None, caption=None, **kwargs):
        super().__init__(
            "table", {"rows": rows, "name": name, "caption": caption}, **kwargs
        )

    def __repr__(self):
        return "Table"

    def render(self) -> Any:
        raise NotImplementedError()
