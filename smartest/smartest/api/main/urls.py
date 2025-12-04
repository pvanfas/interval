from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import notifications, student, teacher

app_name = "api_main"

router = DefaultRouter()

router.register(r"notifications", notifications.NotificationViewSet, basename="notifications")
router.register(r"teacher/assignments", teacher.AssignmentViewSet, basename="teacher_assignments")
router.register(r"teacher/students", teacher.StudentViewSet, basename="teacher_students")
router.register(r"teacher/subjects", teacher.SubjectViewSet, basename="teacher_subjects")
router.register(r"teacher/submissions/assignments", teacher.AssignmentSubmissionViewSet, basename="teacher_assignment_submissions")
# Class Test
router.register(r"teacher/tests", teacher.ClassTestViewSet, basename="teacher_classtests")
router.register(r"teacher/submissions/tests", teacher.TestSubmissionViewSet, basename="teacher_testsubmissions")
router.register(r"teacher/questions/tests", teacher.TestQuestionViewSet, basename="teacher_test_questions")
# Practice Test
router.register(r"teacher/submissions/practices", teacher.PracticeTestSubmissionViewSet, basename="teacher_practice_submissions")
router.register(r"teacher/questions/practices", teacher.PracticeTestQuestionViewSet, basename="teacher_practice_questions")
router.register(r"teacher/practices", teacher.PracticeTestViewSet, basename="teacher_practicestests")
# Mock Test
router.register(r"teacher/submissions/mock", teacher.MockTestSubmissionViewSet, basename="teacher_mock_submissions")
router.register(r"teacher/questions/mock", teacher.MockTestQuestionViewSet, basename="teacher_mock_questions")
router.register(r"teacher/mock", teacher.MockTestViewSet, basename="teacher_mocktests")
# Student
router.register(r"student/tests", student.ClassTestViewSet, basename="student_classtests")
router.register(r"student/assignments", student.AssignmentViewSet, basename="student_assignments")
router.register(r"student/events", student.EventViewset, basename="student_events")
router.register(r"student/practices", student.PracticeTestViewSet, basename="student_practicestests")
router.register(r"student/mock", student.MockTestViewSet, basename="student_mockstests")
router.register(r"student/attempt/mock", student.MockTestSubmissionViewSet, basename="student_mock_submissions")
router.register(r"student/subjects", student.SubjectViewSet, basename="student_subjects")


urlpatterns = [
    path("syllabus/", student.SyllabusListView.as_view(), name="syllabuslist_api"),
    path("teacher/profile/", teacher.TeacherProfileView.as_view(), name="teacher_profile"),
    path("student/profile/", student.StudentProfileView.as_view(), name="student_profile"),
    path("student/upcoming/", student.StudentUpcomingView.as_view(), name="student_upcoming"),
    path("student/progresscard/", student.StudentProgressCardView.as_view(), name="student_progress_card"),
] + router.urls
