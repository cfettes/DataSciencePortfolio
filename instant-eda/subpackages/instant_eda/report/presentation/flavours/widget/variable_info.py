from ipywidgets import widgets

from instant_eda.report.presentation.core import VariableInfo
from instant_eda.report.presentation.flavours.html import templates


class WidgetVariableInfo(VariableInfo):
    def render(self):
        return widgets.HTML(
            templates.template("variable_info.html").render(**self.content)
        )
