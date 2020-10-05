from instant_eda.report.presentation.core import Collapse
from instant_eda.report.presentation.flavours.html import templates


class HTMLCollapse(Collapse):
    def render(self):
        return templates.template("collapse.html").render(**self.content)
