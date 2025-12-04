from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls


schema_view = get_schema_view(
    openapi.Info(title="Little Genie API", default_version="v1", description="Little Genie API"),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include_docs_urls(title="Little Genie API Documentation")),
        path("blogs/", include("blogs.urls", namespace="blogs")),
        path("course/", include("course.urls", namespace="course")),
        path("general/", include("core.urls", namespace="core")),
        path("products/", include("products.urls", namespace="products")),
        path("teams/", include("teams.urls", namespace="teams")),
        path("api/v1/blogs/", include("api.v1.blogs.urls", namespace="api_v1_blogs")),
        path("api/v1/course/", include("api.v1.course.urls", namespace="api_v1_course")),
        path("api/v1/general/", include("api.v1.general.urls", namespace="api_v1_general")),
        path("api/v1/products/", include("api.v1.products.urls", namespace="api_v1_products")),
        path("api/v1/teams/", include("api.v1.teams.urls", namespace="api_v1_teams")),
        path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
        path("tinymce/", include("tinymce.urls")),
        path("accounts/", include("registration.backends.simple.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Little Genie Administration"
admin.site.site_title = "Little Genie Admin Portal"
admin.site.index_title = "Welcome to Little Genie Admin Portal"
