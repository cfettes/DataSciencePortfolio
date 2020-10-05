from IPython.core.display import display
from ipywidgets import Output, widgets

from instant_eda.report.presentation.core.duplicate import Duplicate


class WidgetDuplicate(Duplicate):
    def render(self):
        out = Output()
        with out:
            display(self.content["duplicate"])

        return widgets.VBox([out])
