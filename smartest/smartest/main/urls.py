from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard_view"),
    # Standard
    path("standards/", views.StandardListView.as_view(), name="standard_list"),
    path("standards/create/", views.StandardCreateView.as_view(), name="standard_create"),
    path("standards/detail/<str:pk>/", views.StandardDetailView.as_view(), name="standard_detail"),
    path("standards/update/<str:pk>/", views.StandardUpdateView.as_view(), name="standard_update"),
    path("standards/delete/<str:pk>/", views.StandardDeleteView.as_view(), name="standard_delete"),
    # Subject
    path("subjects/", views.SubjectListView.as_view(), name="subject_list"),
    path("subjects/create/", views.SubjectCreateView.as_view(), name="subject_create"),
    path("subjects/detail/<str:pk>/", views.SubjectDetailView.as_view(), name="subject_detail"),
    path("subjects/update/<str:pk>/", views.SubjectUpdateView.as_view(), name="subject_update"),
    path("subjects/delete/<str:pk>/", views.SubjectDeleteView.as_view(), name="subject_delete"),
    # Teacher
    path("teachers/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teachers/create/", views.TeacherCreateView.as_view(), name="teacher_create"),
    path("teachers/detail/<str:pk>/", views.TeacherDetailView.as_view(), name="teacher_detail"),
    path("teachers/update/<str:pk>/", views.TeacherUpdateView.as_view(), name="teacher_update"),
    path("teachers/delete/<str:pk>/", views.TeacherDeleteView.as_view(), name="teacher_delete"),
    # Student
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("students/create/", views.StudentCreateView.as_view(), name="student_create"),
    path("students/detail/<str:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("students/update/<str:pk>/", views.StudentUpdateView.as_view(), name="student_update"),
    path("students/delete/<str:pk>/", views.StudentDeleteView.as_view(), name="student_delete"),
]
