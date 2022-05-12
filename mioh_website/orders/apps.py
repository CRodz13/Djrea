from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "mioh_website.orders"
    verbose_name = _("Orders")

    def ready(self):
        try:
            import mioh_website.orders.signals  # noqa F401
        except ImportError:
            pass
