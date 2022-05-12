from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home/index.html"), name="home"),
    path("store/home", TemplateView.as_view(template_name="store/store.html"), name="store"),
    path("basket/", TemplateView.as_view(template_name="basket/summary.html"), name="basket_summary"),
    path('account/', include('mioh_website.account.urls', namespace='account')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
