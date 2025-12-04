from django.db import models
from django.utils.crypto import get_random_string
from tinymce.models import HTMLField

from main.base import BaseModel


def gen_assignment_id():
    return "STA-" + get_random_string(length=6).upper()


def gen_test_id():
    return "STT-" + get_random_string(length=6).upper()


class Assignment(BaseModel):
    assignment_id = models.CharField(max_length=200, unique=True, default=gen_assignment_id)
    title = models.CharField(max_length=200)
    question = models.TextField()
    instructions = HTMLField(blank=True, null=True)
    total_marks = models.PositiveIntegerField()
    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    created_by = models.ForeignKey("main.Teacher", on_delete=models.CASCADE, related_name="assignment_created_by")
    subject = models.ForeignKey("main.Subject", on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="assignments/", blank=True, null=True)
    assigned_to = models.ManyToManyField("main.Student", blank=True)

    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"

    # TODO
    def get_progess(self):
        return 0

    def get_submissions(self):
        return self.submissions.all()

    def __str__(self):
        return self.title


class AssignmentSubmission(BaseModel):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey("main.Student", on_delete=models.CASCADE, related_name="assignment_submissions_student")
    attachment = models.FileField(upload_to="assignment_submissions/")
    marks = models.PositiveIntegerField(blank=True, null=True)
    is_valuated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Assignment Submission"
        verbose_name_plural = "Assignment Submissions"

    def __str__(self):
        return f"{self.assignment.title} - {self.student.user.get_full_name()}"


class ClassTest(BaseModel):
    test_id = models.CharField(max_length=200, unique=True, default=gen_test_id)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    test_duration = models.PositiveIntegerField("Test Duration (in minutes)")
    total_marks = models.PositiveIntegerField()
    created_by = models.ForeignKey("main.Teacher", on_delete=models.CASCADE, related_name="class_test_created_by")
    subject = models.ForeignKey("main.Subject", on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField("main.Student", blank=True)
    attachment = models.FileField(upload_to="class_tests/", blank=True, null=True)
    instructions = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = "Class Test"
        verbose_name_plural = "Class Tests"

    # TODO
    def get_progess(self):
        return 0

    def get_submissions(self):
        return self.submissions.all()

    def get_submissions_count(self):
        return self.submissions.count()

    def get_questions(self):
        return self.questions.all()

    def __str__(self):
        return self.title


class TestQuestion(BaseModel):
    test = models.ForeignKey(ClassTest, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    marks = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Test Question"
        verbose_name_plural = "Test Questions"

    def answer_count(self):
        return self.answers.count()

    def get_answers(self):
        return self.answers.all()

    def __str__(self):
        return self.question


class TestAnswer(BaseModel):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name="answers")
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Test Answer"
        verbose_name_plural = "Test Answers"

    def __str__(self):
        return self.answer


class TestSubmission(BaseModel):
    test = models.ForeignKey(ClassTest, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey("main.Student", on_delete=models.CASCADE, related_name="test_submissions_student")
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_started = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_valuated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Test Submission"
        verbose_name_plural = "Test Submissions"

    def get_answers(self):
        return self.answers.all()

    def marks_obtained(self):
        return sum([answer.marks() for answer in self.answers.all()])

    def grade_obtained(self):
        total_marks = self.test.total_marks
        marks_obtained = self.marks_obtained()
        if total_marks == 0:
            return "-"  # Prevent division by zero
        percentage = (marks_obtained / total_marks) * 100
        grade_thresholds = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")]
        for threshold, grade in grade_thresholds:
            if percentage >= threshold:
                return grade
        return "F"

    def answered_count(self):
        return self.answers.count()

    def __str__(self):
        return f"{self.test.title} - {self.student.user.get_full_name()}"


class TestAnswerSubmission(BaseModel):
    submission = models.ForeignKey(TestSubmission, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Test Answer Submission"
        verbose_name_plural = "Test Answer Submissions"

    def marks(self):
        return self.question.marks if self.answer.is_correct else 0

    def __str__(self):
        return f"{self.submission} - {self.question}"


class PracticeTest(BaseModel):
    test_id = models.CharField(max_length=200, unique=True, default=gen_test_id)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    test_duration = models.PositiveIntegerField("Practice Duration (in minutes)")
    total_marks = models.PositiveIntegerField()
    created_by = models.ForeignKey("main.Teacher", on_delete=models.CASCADE, related_name="practice_test_created_by")
    subject = models.ForeignKey("main.Subject", on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="class_tests/", blank=True, null=True)
    instructions = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = "Practice Test"
        verbose_name_plural = "Practice Tests"

    # TODO
    def get_progess(self):
        return 0

    def get_submissions(self):
        return self.submissions.all()

    def get_submissions_count(self):
        return self.submissions.count()

    def get_questions(self):
        return self.questions.all()

    def __str__(self):
        return self.title


class PracticeTestQuestion(BaseModel):
    test = models.ForeignKey(PracticeTest, on_delete=models.CASCADE, related_name="questions")
    question = models.TextField()
    marks = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Practice Question"
        verbose_name_plural = "Practice Questions"

    def answer_count(self):
        return self.answers.count()

    def get_answers(self):
        return self.answers.all()

    def __str__(self):
        return self.question


class PracticeTestAnswer(BaseModel):
    question = models.ForeignKey(PracticeTestQuestion, on_delete=models.CASCADE, related_name="answers")
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Practice Answer"
        verbose_name_plural = "Practice Answers"

    def __str__(self):
        return self.answer


class PracticeTestSubmission(BaseModel):
    test = models.ForeignKey(PracticeTest, on_delete=models.CASCADE, related_name="submissions")
    student = models.ForeignKey("main.Student", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_started = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Practice Submission"
        verbose_name_plural = "Practice Submissions"

    def get_answers(self):
        return self.answers.all()

    def get_question_count(self):
        return self.test.get_questions().count()

    def marks_obtained(self):
        return sum([answer.marks() for answer in self.answers.all()])

    def grade_obtained(self):
        total_marks = self.test.total_marks
        marks_obtained = self.marks_obtained()
        if total_marks == 0:
            return "-"  # Prevent division by zero
        percentage = (marks_obtained / total_marks) * 100
        grade_thresholds = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")]
        for threshold, grade in grade_thresholds:
            if percentage >= threshold:
                return grade
        return "F"

    def answered_count(self):
        return self.answers.count()

    def __str__(self):
        return f"{self.test.title} - {self.student.user.get_full_name()}"


class PracticeTestAnswerSubmission(BaseModel):
    submission = models.ForeignKey(PracticeTestSubmission, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(PracticeTestQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(PracticeTestAnswer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Practice Answer Submission"
        verbose_name_plural = "Practice Answer Submissions"

    def marks(self):
        return self.question.marks if self.answer.is_correct else 0

    def __str__(self):
        return f"{self.submission} - {self.question}"


class Event(BaseModel):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    venue = models.CharField(max_length=200)
    attachment = models.FileField(upload_to="events/", blank=True, null=True)
    content = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class MockTest(BaseModel):
    test_id = models.CharField(max_length=200, unique=True, default=gen_test_id)
    title = models.CharField(max_length=200)
    test_duration = models.PositiveIntegerField("Mock Test Duration (in minutes)")
    total_marks = models.PositiveIntegerField()
    created_by = models.ForeignKey("main.Teacher", on_delete=models.CASCADE, related_name="mock_test_created_by")
    subject = models.ForeignKey("main.Subject", on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="class_tests/", blank=True, null=True)
    instructions = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name = "Mock Test"
        verbose_name_plural = "Mock Tests"

    def get_progess(self):
        return 0

    def get_submissions(self):
        return self.mock_submissions.all()

    def get_submissions_count(self):
        return self.mock_submissions.count()

    def get_questions(self):
        return self.mock_questions.all()

    def __str__(self):
        return self.title


class MockTestQuestion(BaseModel):
    test = models.ForeignKey(MockTest, on_delete=models.CASCADE, related_name="mock_questions")
    question = models.TextField()
    marks = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Mock Question"
        verbose_name_plural = "Mock Questions"

    def answer_count(self):
        return self.get_answers().count()

    def get_answers(self):
        return self.mock_answers.all()

    def __str__(self):
        return self.question


class MockTestAnswer(BaseModel):
    question = models.ForeignKey(MockTestQuestion, on_delete=models.CASCADE, related_name="mock_answers")
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mock Answer"
        verbose_name_plural = "Mock Answers"

    def __str__(self):
        return self.answer


class MockTestSubmission(BaseModel):
    test = models.ForeignKey(MockTest, on_delete=models.CASCADE, related_name="mock_submissions")
    session_id = models.CharField(max_length=200, unique=True, blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    school = models.CharField(max_length=200)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    is_started = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mock Submission"
        verbose_name_plural = "Mock Submissions"

    def get_answers(self):
        return self.mock_answers.all()

    def get_question_count(self):
        return self.test.get_questions().count()

    def marks_obtained(self):
        return sum([answer.marks() for answer in self.get_answers()])

    def grade_obtained(self):
        total_marks = self.test.total_marks
        marks_obtained = self.marks_obtained()
        if total_marks == 0:
            return "-"  # Prevent division by zero
        percentage = (marks_obtained / total_marks) * 100
        grade_thresholds = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")]
        for threshold, grade in grade_thresholds:
            if percentage >= threshold:
                return grade
        return "F"

    def answered_count(self):
        return self.get_answers().count()

    def __str__(self):
        return f"{self.test.title}"


class MockTestAnswerSubmission(BaseModel):
    submission = models.ForeignKey(MockTestSubmission, on_delete=models.CASCADE, related_name="mock_answers")
    question = models.ForeignKey(MockTestQuestion, on_delete=models.CASCADE)
    answer = models.ForeignKey(MockTestAnswer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Mock Answer Submission"
        verbose_name_plural = "Mock Answer Submissions"

    def marks(self):
        return self.question.marks if self.answer.is_correct else 0

    def __str__(self):
        return f"{self.submission} - {self.question}"
