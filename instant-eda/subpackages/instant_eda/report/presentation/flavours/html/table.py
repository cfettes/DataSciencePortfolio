from instant_eda.report.presentation.core.table import Table
from instant_eda.report.presentation.flavours.html import templates


class HTMLTable(Table):
    def render(self):
        return templates.template("table.html").render(**self.content)
