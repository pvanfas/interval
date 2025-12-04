from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = "blogs"

urlpatterns = [
    path("authors/", login_required(views.AuthorList.as_view()), name="author_list"),
    path("new/author/", login_required(views.AuthorForm.as_view()), name="new_author"),
    path("view/author/<str:pk>/", login_required(views.AuthorDetail.as_view()), name="view_author"),
    path("update/author/<str:pk>/", login_required(views.AuthorUpdate.as_view()), name="update_author"),
    path("delete/author/<str:pk>/", login_required(views.AuthorDelete.as_view()), name="delete_author"),
    path("blogs/", login_required(views.BlogList.as_view()), name="blog_list"),
    path("new/blog/", login_required(views.BlogForm.as_view()), name="new_blog"),
    path("view/blog/<str:pk>/", login_required(views.BlogDetail.as_view()), name="view_blog"),
    path("update/blog/<str:pk>/", login_required(views.BlogUpdate.as_view()), name="update_blog"),
    path("delete/blog/<str:pk>/", login_required(views.BlogDelete.as_view()), name="delete_blog"),
]
