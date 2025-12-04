from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Author
from .models import Blog


class AuthorList(ListView):
    queryset = Author.objects.all()


class AuthorDetail(DetailView):
    model = Author
    template_name = "common/object_detail.html"


class AuthorForm(CreateView):
    model = Author
    fields = ["name", "designation", "email", "photo", "about"]
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("blogs:author_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Author"
        return context


class AuthorUpdate(UpdateView):
    model = Author
    fields = ["name", "designation", "email", "photo", "about"]
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Author - "
        return context


class AuthorDelete(DeleteView):
    model = Author
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("blogs:author_list")


class BlogList(ListView):
    queryset = Blog.objects.all()


class BlogDetail(DetailView):
    model = Blog
    template_name = "common/object_detail.html"


class BlogForm(CreateView):
    model = Blog
    fields = [
        "title",
        "author",
        "photo",
        "published_date",
        "published_time",
        "summary",
        "content",
        "is_featured",
        "is_published",
    ]
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("blogs:blog_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Blog"
        return context


class BlogUpdate(UpdateView):
    model = Blog
    fields = [
        "title",
        "author",
        "photo",
        "published_date",
        "published_time",
        "summary",
        "content",
        "is_featured",
        "is_published",
    ]
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Blog -"
        return context


class BlogDelete(DeleteView):
    model = Blog
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("blogs:blog_list")
