from instant_eda.report.presentation.core import FrequencyTableSmall
from instant_eda.report.presentation.flavours.html import templates


class HTMLFrequencyTableSmall(FrequencyTableSmall):
    def render(self):
        return templates.template("frequency_table_small.html").render(**self.content)
