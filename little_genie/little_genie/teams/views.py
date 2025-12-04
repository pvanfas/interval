from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from teams.models import Team


class TeamList(ListView):
    queryset = Team.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_link"] = reverse_lazy("teams:new_team")
        return context


class TeamDetail(DetailView):
    model = Team
    template_name = "common/object_detail.html"


class TeamForm(CreateView):
    model = Team
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("teams:team_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Team"
        return context


class TeamUpdate(UpdateView):
    model = Team
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Team - "
        return context


class TeamDelete(DeleteView):
    model = Team
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("teams:team_list")
