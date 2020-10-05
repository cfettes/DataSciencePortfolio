from instant_eda.report.presentation.core import FrequencyTable
from instant_eda.report.presentation.flavours.html import templates


class HTMLFrequencyTable(FrequencyTable):
    def render(self):
        return templates.template("frequency_table.html").render(**self.content)
