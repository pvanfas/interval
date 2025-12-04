from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("", login_required(views.Index.as_view()), name="index"),
    path("testimonials/", login_required(views.TestimonialList.as_view()), name="testimonial_list"),
    path("new/testimonial/", login_required(views.TestimonialForm.as_view()), name="new_testimonial"),
    path("view/testimonial/<str:pk>/", login_required(views.TestimonialDetail.as_view()), name="view_testimonial"),
    path("update/testimonial/<str:pk>/", login_required(views.TestimonialUpdate.as_view()), name="update_testimonial"),
    path("delete/testimonial/<str:pk>/", login_required(views.TestimonialDelete.as_view()), name="delete_testimonial"),
    path("galleris/", login_required(views.GalleryList.as_view()), name="gallery_list"),
    path("new/gallery/", login_required(views.GalleryForm.as_view()), name="new_gallery"),
    path("view/gallery/<str:pk>/", login_required(views.GalleryDetail.as_view()), name="view_gallery"),
    path("update/gallery/<str:pk>/", login_required(views.GalleryUpdate.as_view()), name="update_gallery"),
    path("delete/gallery/<str:pk>/", login_required(views.GalleryDelete.as_view()), name="delete_gallery"),
    path("contacts/", login_required(views.ContactList.as_view()), name="contact_list"),
    path("new/contact/", login_required(views.ContactForm.as_view()), name="new_contact"),
    path("view/contact/<str:pk>/", login_required(views.ContactDetail.as_view()), name="view_contact"),
    path("update/contact/<str:pk>/", login_required(views.ContactUpdate.as_view()), name="update_contact"),
    path("delete/contact/<str:pk>/", login_required(views.ContactDelete.as_view()), name="delete_contact"),
    path("features/", login_required(views.FeatureList.as_view()), name="feature_list"),
    path("new/feature/", login_required(views.FeatureForm.as_view()), name="new_feature"),
    path("view/feature/<str:pk>/", login_required(views.FeatureDetail.as_view()), name="view_feature"),
    path("update/feature/<str:pk>/", login_required(views.FeatureUpdate.as_view()), name="update_feature"),
    path("delete/feature/<str:pk>/", login_required(views.FeatureDelete.as_view()), name="delete_feature"),
    path("socials/", login_required(views.SocialList.as_view()), name="social_list"),
    path("new/social/", login_required(views.SocialForm.as_view()), name="new_social"),
    path("view/social/<str:pk>/", login_required(views.SocialDetail.as_view()), name="view_social"),
    path("update/social/<str:pk>/", login_required(views.SocialUpdate.as_view()), name="update_social"),
    path("delete/social/<str:pk>/", login_required(views.SocialDelete.as_view()), name="delete_social"),
    path("faqs/", login_required(views.FAQList.as_view()), name="faq_list"),
    path("new/faq/", login_required(views.FAQForm.as_view()), name="new_faq"),
    path("view/faq/<str:pk>/", login_required(views.FAQDetail.as_view()), name="view_faq"),
    path("update/faq/<str:pk>/", login_required(views.FAQUpdate.as_view()), name="update_faq"),
    path("delete/faq/<str:pk>/", login_required(views.FAQDelete.as_view()), name="delete_faq"),
    path("abouts/", login_required(views.AboutList.as_view()), name="about_list"),
    path("view/about/<str:pk>/", login_required(views.AboutDetail.as_view()), name="view_about"),
    path("update/about/<str:pk>/", login_required(views.AboutUpdate.as_view()), name="update_about"),
]
