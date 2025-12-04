from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.utils.translation import gettext_lazy as _


module_urls = i18n_patterns(
    path("admin/", admin.site.urls),
    path("accounts/", include("registration.backends.simple.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("", include("web.urls", namespace="web")),
    path("app/", include("main.urls", namespace="main")),
    prefix_default_language=False,
)

plugin_urls = [path("tinymce/", include("tinymce.urls")), path("i18n/", include("django.conf.urls.i18n"))]

urlpatterns = module_urls + plugin_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

PROJECT_NAME = settings.APP_SETTINGS.get("site_name")
admin.site.site_header = _("%(project_name)s Administration") % {"project_name": PROJECT_NAME}
admin.site.site_title = _("%(project_name)s Admin Portal") % {"project_name": PROJECT_NAME}
admin.site.index_title = _("Welcome to %(project_name)s Admin Portal") % {"project_name": PROJECT_NAME}
