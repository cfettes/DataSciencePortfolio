from instant_eda.report.presentation.core import Variable
from instant_eda.report.presentation.flavours.html import templates


class HTMLVariable(Variable):
    def render(self):
        return templates.template("variable.html").render(**self.content)
