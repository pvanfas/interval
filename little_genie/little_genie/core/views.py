from course.models import CourseEnquiry
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from products.models import ProductEnquiry

from .models import FAQ
from .models import About
from .models import Contact
from .models import Feature
from .models import Gallery
from .models import Social
from .models import Testimonial


class Index(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()[:5]
        context["product_enquiries"] = ProductEnquiry.objects.all()[:5]
        context["course_enquiries"] = CourseEnquiry.objects.all()[:5]
        context["contacts"] = Contact.objects.all()[:5]
        return context


class TestimonialList(ListView):
    queryset = Testimonial.objects.all()


class TestimonialDetail(DetailView):
    model = Testimonial
    template_name = "common/object_detail.html"


class TestimonialForm(CreateView):
    model = Testimonial
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("core:testimonial_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Testimonial"
        return context


class TestimonialUpdate(UpdateView):
    model = Testimonial
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Testimonial - "
        return context


class TestimonialDelete(DeleteView):
    model = Testimonial
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("core:testimonial_list")


class GalleryList(ListView):
    queryset = Gallery.objects.all()


class GalleryDetail(DetailView):
    model = Gallery
    template_name = "common/object_detail.html"


class GalleryForm(CreateView):
    model = Gallery
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("core:gallery_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Gallery"
        return context


class GalleryUpdate(UpdateView):
    model = Gallery
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Gallery -"
        return context


class GalleryDelete(DeleteView):
    model = Gallery
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("core:gallery_list")


class ContactList(ListView):
    queryset = Contact.objects.all()


class ContactDetail(DetailView):
    model = Contact
    template_name = "common/object_detail.html"


class ContactForm(CreateView):
    model = Contact
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("core:contact_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Contact"
        return context


class ContactUpdate(UpdateView):
    model = Contact
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Contact - "
        return context


class ContactDelete(DeleteView):
    model = Contact
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("core:contact_list")


class FeatureList(ListView):
    queryset = Feature.objects.all()


class FeatureDetail(DetailView):
    model = Feature
    template_name = "common/object_detail.html"


class FeatureForm(CreateView):
    model = Feature
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("core:feature_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Feature"
        return context


class FeatureUpdate(UpdateView):
    model = Feature
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Feature - "
        return context


class FeatureDelete(DeleteView):
    model = Feature
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("core:feature_list")


class SocialList(ListView):
    queryset = Social.objects.all()


class SocialDetail(DetailView):
    model = Social
    template_name = "common/object_detail.html"


class SocialForm(CreateView):
    model = Social
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("core:social_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Social"
        return context


class SocialUpdate(UpdateView):
    model = Social
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Social -"
        return context


class SocialDelete(DeleteView):
    model = Social
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("core:social_list")


class FAQList(ListView):
    queryset = FAQ.objects.all()


class FAQDetail(DetailView):
    model = FAQ
    template_name = "common/object_detail.html"


class FAQForm(CreateView):
    model = FAQ
    fields = "__all__"
    template_name = "common/object_form.html"

    def get_success_url(self):
        return reverse_lazy("core:faq_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New FAQ"
        return context


class FAQUpdate(UpdateView):
    model = FAQ
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit FAQ - "
        return context


class FAQDelete(DeleteView):
    model = FAQ
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("core:faq_list")


class AboutList(ListView):
    queryset = About.objects.all()


class AboutDetail(DetailView):
    model = About
    template_name = "common/object_detail.html"


class AboutUpdate(UpdateView):
    model = About
    fields = "__all__"
    template_name = "common/object_form.html"
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit About -"
        return context
