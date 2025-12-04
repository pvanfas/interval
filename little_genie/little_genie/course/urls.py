from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


app_name = "course"

urlpatterns = [
    path("courses/", login_required(views.CourseList.as_view()), name="course_list"),
    path("new/course/", login_required(views.CourseForm.as_view()), name="new_course"),
    path("view/course/<str:pk>/", login_required(views.CourseDetail.as_view()), name="view_course"),
    path("update/course/<str:pk>/", login_required(views.CourseUpdate.as_view()), name="update_course"),
    path("delete/course/<str:pk>/", login_required(views.CourseDelete.as_view()), name="delete_course"),
    path("course_enquiries/", login_required(views.CourseEnquiryList.as_view()), name="course_enquiry_list"),
    path("new/course_enquiry/", login_required(views.CourseEnquiryForm.as_view()), name="new_course_enquiry"),
    path(
        "view/course_enquiry/<str:pk>/", login_required(views.CourseEnquiryDetail.as_view()), name="view_course_enquiry"
    ),
    path(
        "update/course_enquiry/<str:pk>/",
        login_required(views.CourseEnquiryUpdate.as_view()),
        name="update_course_enquiry",
    ),
    path(
        "delete/course_enquiry/<str:pk>/",
        login_required(views.CourseEnquiryDelete.as_view()),
        name="delete_course_enquiry",
    ),
]
