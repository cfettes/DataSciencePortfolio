from instant_eda.report.presentation.core import ToggleButton
from instant_eda.report.presentation.flavours.html import templates


class HTMLToggleButton(ToggleButton):
    def render(self):
        return templates.template("toggle_button.html").render(**self.content)
