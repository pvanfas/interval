from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = "teams"

urlpatterns = [
    path("teams/", login_required(views.TeamList.as_view()), name="team_list"),
    path("new/team/", login_required(views.TeamForm.as_view()), name="new_team"),
    path("view/team/<str:pk>/", login_required(views.TeamDetail.as_view()), name="view_team"),
    path("update/team/<str:pk>/", login_required(views.TeamUpdate.as_view()), name="update_team"),
    path("delete/team/<str:pk>/", login_required(views.TeamDelete.as_view()), name="delete_team"),
]
