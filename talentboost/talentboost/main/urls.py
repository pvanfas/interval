from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard_view"),
    # Coupon
    path("coupons/", views.CouponListView.as_view(), name="coupon_list"),
    path("coupons/create/", views.CouponCreateView.as_view(), name="coupon_create"),
    path("coupons/detail/<str:pk>/", views.CouponDetailView.as_view(), name="coupon_detail"),
    path("coupons/update/<str:pk>/", views.CouponUpdateView.as_view(), name="coupon_update"),
    path("coupons/delete/<str:pk>/", views.CouponDeleteView.as_view(), name="coupon_delete"),
    # Document
    path("documents/", views.DocumentListView.as_view(), name="document_list"),
    path("documents/create/", views.DocumentCreateView.as_view(), name="document_create"),
    path("documents/detail/<str:pk>/", views.DocumentDetailView.as_view(), name="document_detail"),
    path("documents/update/<str:pk>/", views.DocumentUpdateView.as_view(), name="document_update"),
    path("documents/delete/<str:pk>/", views.DocumentDeleteView.as_view(), name="document_delete"),
    # School
    path("schools/", views.SchoolListView.as_view(), name="school_list"),
    path("schools/create/", views.SchoolCreateView.as_view(), name="school_create"),
    path("schools/detail/<str:pk>/", views.SchoolDetailView.as_view(), name="school_detail"),
    path("schools/update/<str:pk>/", views.SchoolUpdateView.as_view(), name="school_update"),
    path("schools/delete/<str:pk>/", views.SchoolDeleteView.as_view(), name="school_delete"),
    # StudentRegistration
    path("student-registrations/", views.StudentRegistrationListView.as_view(), name="student_registration_list"),
    path("student-registrations/create/", views.StudentRegistrationCreateView.as_view(), name="student_registration_create"),
    path("student-registrations/detail/<str:pk>/", views.StudentRegistrationDetailView.as_view(), name="student_registration_detail"),
    path("student-registrations/resend/<str:pk>/", views.StudentRegistrationResendView.as_view(), name="student_registration_resend"),
    path("student-registrations/update/<str:pk>/", views.StudentRegistrationUpdateView.as_view(), name="student_registration_update"),
    path("student-registrations/delete/<str:pk>/", views.StudentRegistrationDeleteView.as_view(), name="student_registration_delete"),
    # Manage Data
    path("manage/import/", views.ManageImportView.as_view(), name="manage_import"),
    path("complete/import/<str:pk>/", views.CompleteImportView.as_view(), name="complete_import"),
    path("status/import/<str:pk>/", views.StatusImportView.as_view(), name="status_import"),
]
