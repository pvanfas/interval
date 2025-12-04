from rest_framework import serializers

from main.models import Student, Subject, Syllabus
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
    PracticeTestSubmission,
    TestAnswer,
    TestAnswerSubmission,
    TestQuestion,
    TestSubmission,
)


class SyllabusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syllabus
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    assignments = serializers.SerializerMethodField()
    tests = serializers.SerializerMethodField()
    syllabus_name = serializers.SerializerMethodField()

    def get_assignments(self, obj):
        student = self.context["request"].user.student
        assignemnts = Assignment.objects.filter(subject=obj)
        return {
            "total": assignemnts.count(),
            "submitted": AssignmentSubmission.objects.filter(assignment__in=assignemnts, student=student).count(),
        }

    def get_tests(self, obj):
        student = self.context["request"].user.student
        tests = ClassTest.objects.filter(subject=obj)
        return {
            "total": tests.count(),
            "submitted": TestSubmission.objects.filter(test__in=tests, student=student).count(),
        }

    def get_syllabus_name(self, obj):
        return obj.syllabus.name

    class Meta:
        depth = 0
        model = Subject
        fields = ("id", "name", "syllabus", "syllabus_name", "code", "assignments", "tests")


class StudenProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    standard_id = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    marks = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    class_avg = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.user.get_photo()

    def get_marks(self, obj):
        return obj.get_marks()

    def get_grade(self, obj):
        return obj.get_grade()

    def get_standard_id(self, obj):
        return obj.standard.id

    def get_class_avg(self, obj):
        return "30/50"

    def get_subjects(self, obj):
        request = self.context.get("request", None)
        if request:
            context = {"request": request}
            return SubjectSerializer(obj.standard.subjects, many=True, context=context).data
        return []

    class Meta:
        depth = 0
        model = Student
        fields = ("id", "student_id", "user", "standard", "standard_id", "photo", "marks", "grade", "class_avg", "subjects")


class StudentDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    standard_id = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    marks = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    class_avg = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.user.get_photo()

    def get_marks(self, obj):
        return obj.get_marks()

    def get_grade(self, obj):
        return obj.get_grade()

    def get_standard_id(self, obj):
        return obj.standard.id

    def get_class_avg(self, obj):
        return "30/50"

    class Meta:
        depth = 0
        model = Student
        fields = ("id", "student_id", "user", "standard", "standard_id", "photo", "marks", "grade", "class_avg")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 0
        model = Event
        fields = "__all__"


class ClassTestListSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    is_submitted = serializers.SerializerMethodField()

    def get_is_submitted(self, obj):
        student = self.context["request"].user.student
        return TestSubmission.objects.filter(test=obj, student=student).exists()

    class Meta:
        depth = 0
        model = ClassTest
        fields = ("id", "test_id", "title", "instructions", "due_date", "created_by", "subject", "created_at", "test_duration", "total_marks", "attachment", "is_submitted")


class TestSubmissionListSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    student = serializers.StringRelatedField()
    student_id = serializers.SerializerMethodField()
    student_pk = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_student_pk(self, obj):
        return obj.student.pk

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = TestSubmission
        fields = ("id", "test", "student", "student_id", "student_pk", "started_at", "marks_obtained", "grade_obtained", "answered_count")


class ClassTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswer
        fields = ("id", "answer")


class ClassTestQuestionSerializer(serializers.ModelSerializer):
    answers = ClassTestAnswerSerializer(many=True)

    class Meta:
        model = TestQuestion
        fields = ("id", "question", "marks", "answers")


class ClassTestDetailSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    subject_id = serializers.SerializerMethodField()
    questions = ClassTestQuestionSerializer(many=True)
    progress = serializers.SerializerMethodField()
    is_submitted = serializers.SerializerMethodField()

    def get_is_submitted(self, obj):
        student = self.context["request"].user.student
        return TestSubmission.objects.filter(test=obj, student=student).exists()

    def get_questions(self, obj):
        return obj.get_questions()

    def get_progress(self, obj):
        student = self.context["request"].user.student
        submission = TestSubmission.objects.filter(test=obj, student=student).first()
        if submission:
            return submission.marks_obtained()
        return 0

    def get_subject_id(self, obj):
        return obj.subject.id

    class Meta:
        depth = 0
        model = ClassTest
        fields = (
            "id",
            "test_id",
            "title",
            "instructions",
            "due_date",
            "created_by",
            "subject",
            "subject_id",
            "created_at",
            "progress",
            "test_duration",
            "total_marks",
            "attachment",
            "is_submitted",
            "questions",
        )


class AssignmentDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    subject_id = serializers.SerializerMethodField()
    is_submitted = serializers.SerializerMethodField()
    submissions = serializers.SerializerMethodField()

    def get_submissions(self, obj):
        student = self.context["request"].user.student
        submissions = AssignmentSubmission.objects.filter(assignment=obj, student=student)
        return AssignmentSubmissionSerializer(submissions, many=True).data

    def get_is_submitted(self, obj):
        student = self.context["request"].user.student
        return AssignmentSubmission.objects.filter(assignment=obj, student=student).exists()

    def get_subject_id(self, obj):
        return obj.subject.id

    class Meta:
        depth = 0
        model = Assignment
        fields = (
            "id",
            "assignment_id",
            "title",
            "question",
            "instructions",
            "assigned_date",
            "due_date",
            "created_by",
            "subject",
            "subject_id",
            "total_marks",
            "attachment",
            "is_submitted",
            "submissions",
        )


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    assignment = serializers.StringRelatedField()
    student = serializers.StringRelatedField()
    student_id = serializers.SerializerMethodField()

    def get_student_id(self, obj):
        return obj.student.student_id

    class Meta:
        depth = 1
        model = AssignmentSubmission
        fields = ("id", "assignment", "student", "student_id", "marks", "attachment", "is_valuated", "timestamp")


class TestAnswerSubmissionSerializer(serializers.ModelSerializer):
    submission = serializers.StringRelatedField()
    submission_id = serializers.SerializerMethodField()
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.test.id

    def get_submission_id(self, obj):
        return obj.submission.id

    class Meta:
        model = TestAnswerSubmission
        fields = ("id", "submission", "submission_id", "test", "test_id", "question", "answer")


class PracticeTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeTestAnswer
        fields = ("id", "answer", "is_correct")


class PracticeTestQuestionSerializer(serializers.ModelSerializer):
    answers = PracticeTestAnswerSerializer(many=True)

    class Meta:
        model = PracticeTestQuestion
        fields = ("id", "question", "marks", "answers")

    def create(self, validated_data):
        answers_data = validated_data.pop("answers")
        test_question = PracticeTestQuestion.objects.create(**validated_data)
        for answer_data in answers_data:
            PracticeTestAnswer.objects.create(question=test_question, **answer_data)
        return test_question

    def update(self, instance, validated_data):
        instance.question = validated_data.get("question", instance.question)
        instance.marks = validated_data.get("marks", instance.marks)
        instance.save()
        answers_data = validated_data.pop("answers", [])
        instance.answers.all().delete()
        for answer_data in answers_data:
            PracticeTestAnswer.objects.create(question=instance, **answer_data)
        return instance


class PracticeTestDetailSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    subject_id = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    questions = PracticeTestQuestionSerializer(many=True)

    def get_questions(self, obj):
        return obj.get_questions()

    def get_progress(self, obj):
        student = self.context["request"].user.student
        submission = PracticeTestSubmission.objects.filter(test=obj, student=student).first()
        if submission:
            return submission.marks_obtained()
        return 0

    def get_subject_id(self, obj):
        return obj.subject.pk

    class Meta:
        depth = 0
        model = PracticeTest
        fields = (
            "id",
            "test_id",
            "title",
            "instructions",
            "due_date",
            "created_by",
            "subject",
            "subject_id",
            "created_at",
            "progress",
            "test_duration",
            "total_marks",
            "attachment",
            "questions",
        )


class PracticeTestListSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    class Meta:
        depth = 0
        model = PracticeTest
        fields = ("id", "test_id", "title", "instructions", "due_date", "created_by", "subject", "created_at", "test_duration", "total_marks", "attachment")


class PracticeTestAnswerSubmissionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    answer = serializers.StringRelatedField()
    marks = serializers.SerializerMethodField(read_only=True)

    def get_marks(self, obj):
        return obj.question.marks if obj.answer.is_correct else 0

    class Meta:
        model = PracticeTestAnswerSubmission
        fields = ("id", "question", "answer", "marks")


class PracticeTestSubmissionDetailSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    student = serializers.StringRelatedField()
    student_id = serializers.SerializerMethodField()
    student_pk = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()
    answers = PracticeTestAnswerSubmissionSerializer(many=True)

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_student_pk(self, obj):
        return obj.student.pk

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = PracticeTestSubmission
        fields = ("id", "test", "student", "student_id", "student_pk", "started_at", "marks_obtained", "grade_obtained", "answered_count", "answers")


class PracticeTestSubmissionListSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()
    submission = serializers.StringRelatedField()
    submission_id = serializers.SerializerMethodField()
    student = serializers.StringRelatedField()
    student_id = serializers.SerializerMethodField()
    student_pk = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.test.id

    def get_submission_id(self, obj):
        return obj.id

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_student_pk(self, obj):
        return obj.student.pk

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = PracticeTestSubmission
        fields = ("id", "test", "test_id", "submission", "submission_id", "student", "student_id", "student_pk", "started_at", "marks_obtained", "grade_obtained", "answered_count")


class PracticeTestAnswerSubmissionSerializer(serializers.ModelSerializer):
    submission = serializers.StringRelatedField()
    submission_id = serializers.SerializerMethodField()
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.submission.test.id

    def get_submission_id(self, obj):
        return obj.submission.id

    class Meta:
        model = PracticeTestAnswerSubmission
        fields = ("id", "test", "test_id", "submission", "submission_id", "question", "answer")


class PracticeResultSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()
    question_count = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.id

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    def get_question_count(self, obj):
        return obj.get_question_count()

    class Meta:
        model = PracticeTestSubmission
        fields = ("id", "test", "test_id", "marks_obtained", "grade_obtained", "answered_count", "question_count")


# MockTest


class MockTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTestAnswer
        fields = ("id", "answer", "is_correct")


class MockTestQuestionSerializer(serializers.ModelSerializer):
    answers = MockTestAnswerSerializer(many=True, source="mock_answers")

    class Meta:
        model = MockTestQuestion
        fields = ("id", "question", "marks", "answers")

    def create(self, validated_data):
        answers_data = validated_data.pop("mock_answers")
        test_question = MockTestQuestion.objects.create(**validated_data)
        for answer_data in answers_data:
            MockTestAnswer.objects.create(question=test_question, **answer_data)
        return test_question

    def update(self, instance, validated_data):
        instance.question = validated_data.get("question", instance.question)
        instance.marks = validated_data.get("marks", instance.marks)
        instance.save()
        answers_data = validated_data.pop("mock_answers", [])
        instance.answers.all().delete()
        for answer_data in answers_data:
            MockTestAnswer.objects.create(question=instance, **answer_data)
        return instance


class MockTestDetailSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    subject_id = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    questions = MockTestQuestionSerializer(many=True, source="mock_questions")

    def get_questions(self, obj):
        return obj.get_questions()

    def get_progress(self, obj):
        request = self.context.get("request", None)
        session_id = request.session.session_key if request else None
        submission = MockTestSubmission.objects.filter(test=obj, session_id=session_id).first()
        if submission:
            return submission.marks_obtained()
        return 0

    def get_subject_id(self, obj):
        return obj.subject.pk

    class Meta:
        depth = 0
        model = MockTest
        fields = (
            "id",
            "test_id",
            "title",
            "instructions",
            "created_by",
            "subject",
            "subject_id",
            "created_at",
            "progress",
            "test_duration",
            "total_marks",
            "attachment",
            "questions",
        )


class MockTestListSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    class Meta:
        depth = 0
        model = MockTest
        fields = ("id", "test_id", "title", "instructions", "created_by", "subject", "created_at", "test_duration", "total_marks", "attachment")


class MockTestAnswerSubmissionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    answer = serializers.StringRelatedField()
    marks = serializers.SerializerMethodField(read_only=True)

    def get_marks(self, obj):
        return obj.question.marks if obj.answer.is_correct else 0

    class Meta:
        model = MockTestAnswerSubmission
        fields = ("id", "question", "answer", "marks")


class MockTestSubmissionDetailSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()
    answers = MockTestAnswerSubmissionSerializer(many=True)

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_student_pk(self, obj):
        return obj.student.pk

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = MockTestSubmission
        fields = ("id", "test", "session_id", "started_at", "marks_obtained", "grade_obtained", "answered_count", "answers")


class MockTestSubmissionListSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()
    submission = serializers.StringRelatedField()
    submission_id = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.test.id

    def get_submission_id(self, obj):
        return obj.id

    def get_student_id(self, obj):
        return obj.student.student_id

    def get_student_pk(self, obj):
        return obj.student.pk

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = MockTestSubmission
        fields = ("id", "test", "test_id", "submission", "submission_id", "session_id", "started_at", "marks_obtained", "grade_obtained", "answered_count")


class MockTestSubmissionStartSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.test.id

    class Meta:
        model = MockTestSubmission
        fields = ("id", "test", "test_id", "name", "email", "mobile_number", "started_at", "session_id")


class MockTestAnswerSubmissionSerializer(serializers.ModelSerializer):
    submission = serializers.StringRelatedField()
    submission_id = serializers.SerializerMethodField()
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.submission.test.id

    def get_submission_id(self, obj):
        return obj.submission.id

    class Meta:
        model = MockTestAnswerSubmission
        fields = ("id", "test", "test_id", "submission", "submission_id", "question", "answer")


class MockResultSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    test_id = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()
    question_count = serializers.SerializerMethodField()

    def get_test_id(self, obj):
        return obj.id

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    def get_question_count(self, obj):
        return obj.get_question_count()

    class Meta:
        model = MockTestSubmission
        fields = ("id", "test", "test_id", "marks_obtained", "grade_obtained", "answered_count", "question_count")
