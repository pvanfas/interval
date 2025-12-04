from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from web.views import HomeView

schema_view = get_schema_view(title="Smartest API")


module_urls = i18n_patterns(
    path("api/docs/", include_docs_urls(title="Smartest API Documentation", public=True)),
    path("api/users/", include("api.users.urls")),
    path("api/users/password_reset/", include("django_rest_passwordreset.urls", namespace="password_reset")),
    path("api/main/", include("api.main.urls")),
    path("accounts/", include("registration.backends.simple.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("app/", include("web.urls", namespace="web")),
    path("app/", include("main.urls", namespace="main")),
    path("", HomeView.as_view(), name="home"),
    prefix_default_language=False,
)

plugin_urls = [
    path("admin/", admin.site.urls),
    path("tinymce/", include("tinymce.urls")),
    path("translate/", include("rosetta.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns = module_urls + plugin_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

PROJECT_NAME = settings.APP_SETTINGS.get("site_name")
admin.site.site_header = _("%(project_name)s Administration") % {"project_name": PROJECT_NAME}
admin.site.site_title = _("%(project_name)s Admin Portal") % {"project_name": PROJECT_NAME}
admin.site.index_title = _("Welcome to %(project_name)s Admin Portal") % {"project_name": PROJECT_NAME}
