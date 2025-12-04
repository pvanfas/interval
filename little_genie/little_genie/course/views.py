from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Course
from .models import CourseEnquiry


class CourseList(ListView):
    queryset = Course.objects.all()


class CourseDetail(DetailView):
    model = Course
    template_name = "common/object_detail.html"


class CourseForm(CreateView):
    model = Course
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("course:course_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Course"
        return context


class CourseUpdate(UpdateView):
    model = Course
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Course - "
        return context


class CourseDelete(DeleteView):
    model = Course
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("course:course_list")


class CourseEnquiryList(ListView):
    queryset = CourseEnquiry.objects.all()


class CourseEnquiryDetail(DetailView):
    model = CourseEnquiry
    template_name = "common/object_detail.html"


class CourseEnquiryForm(CreateView):
    model = CourseEnquiry
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("course:course_enquiry_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Course Enquiry"
        return context


class CourseEnquiryUpdate(UpdateView):
    model = CourseEnquiry
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Course Enquiry -"
        return context


class CourseEnquiryDelete(DeleteView):
    model = CourseEnquiry
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("course:course_enquiry_list")
