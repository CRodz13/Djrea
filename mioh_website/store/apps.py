from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "mioh_website.store"
    verbose_name = _("Store")

    def ready(self):
        try:
            import mioh_website.users.signals  # noqa F401
        except ImportError:
            pass
