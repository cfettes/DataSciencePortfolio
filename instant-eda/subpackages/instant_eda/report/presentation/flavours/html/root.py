from instant_eda.report.presentation.core.root import Root
from instant_eda.report.presentation.flavours.html import templates


class HTMLRoot(Root):
    def render(self, **kwargs):
        nav_items = [
            (section.name, section.anchor_id)
            for section in self.content["body"].content["items"]
        ]

        return templates.template("report.html").render(
            **self.content, nav_items=nav_items, **kwargs
        )
