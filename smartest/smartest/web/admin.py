from django.contrib import admin

from main.base import BaseAdmin
from web.models import (
    Assignment,
    AssignmentSubmission,
    ClassTest,
    Event,
    MockTest,
    MockTestAnswer,
    MockTestAnswerSubmission,
    MockTestQuestion,
    MockTestSubmission,
    PracticeTest,
    PracticeTestAnswer,
    PracticeTestAnswerSubmission,
    PracticeTestQuestion,
    TestAnswer,
    TestAnswerSubmission,
    TestQuestion,
    TestSubmission,
)


class PracticeTestQuestionInline(admin.TabularInline):
    model = PracticeTestQuestion
    exclude = ("is_active",)


class PracticeTestAnswerInline(admin.TabularInline):
    model = PracticeTestAnswer
    exclude = ("is_active",)


class MockTestAnswerInline(admin.TabularInline):
    model = MockTestAnswer
    exclude = ("is_active",)


class PracticeTestAnswerSubmissionInline(admin.TabularInline):
    model = PracticeTestAnswerSubmission
    exclude = ("is_active",)


class TestQuestionInline(admin.TabularInline):
    model = TestQuestion
    exclude = ("is_active",)


class TestAnswerInline(admin.TabularInline):
    model = TestAnswer
    exclude = ("is_active",)


class TestAnswerSubmissionInline(admin.TabularInline):
    model = TestAnswerSubmission
    exclude = ("is_active",)


class MockTestQuestionInline(admin.TabularInline):
    model = MockTestQuestion
    exclude = ("is_active",)


class MockAnswerInline(admin.TabularInline):
    model = MockTestAnswer
    exclude = ("is_active",)


class MockTestSubmissionInline(admin.TabularInline):
    model = MockTestSubmission
    exclude = ("is_active",)


class MockTestAnswerSubmissionInline(admin.TabularInline):
    model = MockTestAnswerSubmission
    exclude = ("is_active",)


@admin.register(TestQuestion)
class TestQuestionAdmin(BaseAdmin):
    inlines = [TestAnswerInline]
    list_display = ("question", "marks", "answer_count")
    list_filter = ("test",)


@admin.register(ClassTest)
class ClassTestAdmin(BaseAdmin):
    autocomplete_fields = ("created_by", "subject")
    list_display = ("title", "created_by", "subject")
    inlines = [TestQuestionInline]
    search_fields = ("title", "instructions")


@admin.register(Assignment)
class AssignmentAdmin(BaseAdmin):
    autocomplete_fields = ("created_by", "subject")
    list_display = ("title", "created_by", "subject")
    search_fields = ("title", "instructions")


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(BaseAdmin):
    list_display = ("assignment", "student", "marks", "timestamp")
    autocomplete_fields = ("assignment", "student")
    search_fields = ("assignment__title", "student__user__first_name", "student__user__last_name")


@admin.register(TestSubmission)
class TestSubmissionAdmin(BaseAdmin):
    list_display = ("test", "student", "marks_obtained")
    autocomplete_fields = ("test", "student")
    inlines = [TestAnswerSubmissionInline]


@admin.register(PracticeTestQuestion)
class PracticeTestQuestionAdmin(BaseAdmin):
    inlines = [PracticeTestAnswerInline]
    list_display = ("question", "marks", "answer_count")
    list_filter = ("test",)


@admin.register(PracticeTest)
class PracticeTestAdmin(BaseAdmin):
    autocomplete_fields = ("created_by", "subject")
    list_display = ("title", "created_by", "subject")
    inlines = [PracticeTestQuestionInline]
    search_fields = ("title", "instructions")


@admin.register(Event)
class EventAdmin(BaseAdmin):
    pass


# @admin.register(PracticeTestAnswer)
# class PracticeTestAnswerAdmin(BaseAdmin):
#     pass


@admin.register(MockTest)
class MockTestAdmin(BaseAdmin):
    list_display = ("title", "created_by", "subject")
    autocomplete_fields = ("created_by", "subject")
    search_fields = ("title", "instructions")
    inlines = [MockTestQuestionInline]
    list_filter = ("subject",)


@admin.register(MockTestQuestion)
class MockTestQuestionAdmin(BaseAdmin):
    inlines = [MockTestAnswerInline]
    list_display = ("question", "marks", "answer_count")
    list_filter = ("test",)


@admin.register(MockTestSubmission)
class MockTestSubmissionAdmin(BaseAdmin):
    list_display = ("test", "session_id", "started_at", "completed_at", "marks_obtained")
    autocomplete_fields = ("test",)
    inlines = [MockTestAnswerSubmissionInline]
