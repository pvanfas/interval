from django.urls import path

from . import views

app_name = "web"


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("tools/", views.tools, name="tools"),
    path("courses/", views.academic_courses, name="academic_courses"),
    path("language-courses/", views.language_courses, name="language_courses"),
    path("nonacademics/", views.nonacademics, name="nonacademics"),
    path("clubs/", views.clubs, name="clubs"),
    path("news/", views.news, name="news"),
    path("testimonials/", views.testimonials, name="testimonials"),
    path("blogs/", views.blogs, name="blogs"),
    path("contact/", views.contact, name="contact"),
    path("subjects/", views.subjects, name="subjects"),
    path("boards/", views.boards, name="boards"),
    path("countries/", views.countries, name="countries"),
    path("downloads/", views.downloads, name="downloads"),
    path("terms-and-conditions/", views.terms_and_conditions, name="terms_and_conditions"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("thanks/", views.thanks, name="thanks"),
    path("save_booking/", views.save_booking, name="save_booking"),
    path("smartest/search/", views.smartest_search, name="smartest_search"),
    # Detail views
    path("blog/category/<str:slug>/", views.blog_category_detail, name="blog_category_detail"),
    path("courses/<str:slug>/", views.course_detail, name="course_detail"),
    path("nonacademic-courses/<str:slug>/", views.nac_course_detail, name="nac_course_detail"),
    path("news/<str:slug>/", views.news_detail, name="news_detail"),
    path("blogs/<str:slug>/", views.blog_detail, name="blog_detail"),
    path("location/<str:slug>/", views.location_detail, name="location_detail"),
    path("subject/<str:slug>/", views.subject_detail, name="subject_detail"),
    path("city/<str:slug>/", views.city_detail, name="city_detail"),
    path("board/<str:slug>/", views.board_detail, name="board_detail"),
    # payment
    path("courses/<str:slug>/form/", views.course_form, name="course_form"),
    path("pay/<str:pk>/payment/", views.course_payment, name="course_payment"),
    path("pay/<str:pk>/payment/callback/", views.payment_callback, name="payment_callback"),
    path("verify/", views.verify, name="verify"),
    path("tools/kerala-sslc-grade-to-percentage-calculator-2025/", views.kerala_sslc_calculator, name="kerala_sslc_calculator"),
    path("tools/tamilnadu-sslc-grade-to-percentage-calculator-2025/", views.tamilnadu_sslc_calculator, name="tamilnadu_sslc_calculator"),
    path("tools/cbse-cgpa-to-percentage-calculator-for-class-10/", views.cbse_calculator, name="cbse_calculator"),
    path("tools/cbse-class-12-cgpa-to-percentage-calculator/", views.cbse_calculator_12, name="cbse_calculator_12"),
    path("tools/kerala-class-12-plus-two-percentage-calculation/", views.kerala_hsc_calculator, name="kerala_hsc_calculator"),
    path("tools/tamilnadu-class-12-plus-two-percentage-calculation/", views.tamilnadu_hsc_calculator, name="tamilnadu_hsc_calculator"),
]
