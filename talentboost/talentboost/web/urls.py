from django.urls import path

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    # student_application
    path("student/application/", views.student_application, name="student_application"),
    path("student/payment/<str:pk>/", views.student_payment, name="student_payment"),
    path("student/callback/<str:pk>/", views.student_callback, name="student_callback"),
    path("student/thanks/<str:pk>/", views.student_thanks, name="student_thanks"),
    # school application
    path("school/registration/", views.school_registration, name="school_registration"),
    path("school/payment/<str:pk>/", views.school_payment, name="school_payment"),
    path("school/thanks/<str:pk>/", views.school_thanks, name="school_thanks"),
]
