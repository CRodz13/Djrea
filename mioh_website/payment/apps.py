from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "mioh_website.payment"
    verbose_name = _("Payment")

    def ready(self):
        try:
            import mioh_website.payment.signals  # noqa F401
        except ImportError:
            pass
