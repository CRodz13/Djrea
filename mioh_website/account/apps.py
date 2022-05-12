from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "mioh_website.account"
    verbose_name = _("Account")

    def ready(self):
        try:
            import mioh_website.account.signals  # noqa F401
        except ImportError:
            pass
