from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "mioh_website.basket"
    verbose_name = _("Basket")

    def ready(self):
        try:
            import mioh_website.basket.signals  # noqa F401
        except ImportError:
            pass
