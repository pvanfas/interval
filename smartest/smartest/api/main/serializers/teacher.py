from rest_framework import serializers

from main.models import Notification, Standard, Student, Subject, Teacher
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


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    photo = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    total_classes = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.user.get_photo()

    def get_total_students(self, obj):
        return obj.get_total_students()

    def get_total_classes(self, obj):
        return obj.get_total_classes()

    def get_subjects(self, obj):
        return SubjectSerializer(obj.subjects.all(), many=True).data

    class Meta:
        depth = 1
        model = Teacher
        fields = ("user", "photo", "total_students", "total_classes", "subjects")


class StudentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    photo = serializers.SerializerMethodField()
    progress_card_url = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.user.get_photo()

    def get_progress_card_url(self, obj):
        return ""

    class Meta:
        depth = 0
        model = Student
        fields = ("id", "student_id", "user", "standard", "photo", "progress_card_url")


class AssignmentListSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    progress = serializers.SerializerMethodField()
    assigned_count = serializers.SerializerMethodField()

    def get_assigned_count(self, obj):
        return obj.assigned_to.count()

    def get_progress(self, obj):
        return ""

    class Meta:
        depth = 0
        model = Assignment
        fields = (
            "id",
            "assignment_id",
            "title",
            "question",
            "instructions",
            "total_marks",
            "assigned_date",
            "due_date",
            "created_by",
            "subject",
            "attachment",
            "progress",
            "assigned_count",
        )


class AssignmentDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    progress = serializers.SerializerMethodField()
    assigned_to = StudentListSerializer(many=True, required=False)
    assigned_count = serializers.SerializerMethodField()

    def get_assigned_count(self, obj):
        return obj.assigned_to.count()

    # TODO
    def get_progress(self, obj):
        return ""

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
            "progress",
            "total_marks",
            "attachment",
            "assigned_count",
            "assigned_to",
        )


class AssignmentCreateSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True, required=False)
    created_by = serializers.StringRelatedField()
    assigned_count = serializers.SerializerMethodField()

    def get_assigned_count(self, obj):
        return obj.assigned_to.count()

    # TODO
    def get_progress(self, obj):
        return ""

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
            "progress",
            "total_marks",
            "attachment",
            "assigned_count",
            "assigned_to",
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


class ClassTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswer
        fields = ("id", "answer", "is_correct")


class ClassTestQuestionSerializer(serializers.ModelSerializer):
    answers = ClassTestAnswerSerializer(many=True)

    class Meta:
        model = TestQuestion
        fields = ("id", "question", "marks", "answers")

    def create(self, validated_data):
        answers_data = validated_data.pop("answers")
        test_question = TestQuestion.objects.create(**validated_data)
        for answer_data in answers_data:
            TestAnswer.objects.create(question=test_question, **answer_data)
        return test_question

    def update(self, instance, validated_data):
        instance.question = validated_data.get("question", instance.question)
        instance.marks = validated_data.get("marks", instance.marks)
        instance.save()
        answers_data = validated_data.pop("answers", [])
        instance.answers.all().delete()
        for answer_data in answers_data:
            TestAnswer.objects.create(question=instance, **answer_data)
        return instance


class ClassTestListSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    submissions_count = serializers.SerializerMethodField()

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    class Meta:
        depth = 0
        model = ClassTest
        fields = ("id", "test_id", "title", "instructions", "due_date", "created_by", "subject", "created_at", "test_duration", "total_marks", "attachment", "submissions_count")


class ClassTestDetailSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    questions = ClassTestQuestionSerializer(many=True)
    progress = serializers.SerializerMethodField()
    assigned_to = StudentListSerializer(many=True, required=False)
    submissions_count = serializers.SerializerMethodField()

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    def get_questions(self, obj):
        return obj.get_questions()

    # TODO
    def get_progress(self, obj):
        return ""

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
            "created_at",
            "progress",
            "test_duration",
            "total_marks",
            "attachment",
            "questions",
            "assigned_to",
            "submissions_count",
        )


class ClassTestCreateSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), many=True, required=False)
    created_by = serializers.StringRelatedField()

    # TODO
    def get_progress(self, obj):
        return ""

    class Meta:
        depth = 0
        model = ClassTest
        fields = (
            "id",
            "test_id",
            "title",
            "instructions",
            "due_date",
            "subject",
            "created_by",
            "test_duration",
            "total_marks",
            "attachment",
            "progress",
            "assigned_to",
        )


class TestAnswerSubmissionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    answer = serializers.StringRelatedField()
    marks = serializers.SerializerMethodField()

    def get_marks(self, obj):
        return obj.question.marks if obj.answer.is_correct else 0

    class Meta:
        model = TestAnswerSubmission
        fields = ("id", "question", "answer", "marks")


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


class TestSubmissionDetailSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    student = serializers.StringRelatedField()
    student_id = serializers.SerializerMethodField()
    student_pk = serializers.SerializerMethodField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()
    answers = TestAnswerSubmissionSerializer(many=True)

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
        fields = ("id", "test", "student", "student_id", "student_pk", "started_at", "marks_obtained", "grade_obtained", "answered_count", "answers")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 0
        model = Event
        fields = "__all__"


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


class PracticeTestListSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    submissions_count = serializers.SerializerMethodField()

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    class Meta:
        depth = 0
        model = PracticeTest
        fields = ("id", "test_id", "title", "instructions", "due_date", "created_by", "subject", "created_at", "test_duration", "total_marks", "attachment", "submissions_count")


class PracticeTestDetailSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    subject_id = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    submissions_count = serializers.SerializerMethodField()
    questions = PracticeTestQuestionSerializer(many=True)

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    def get_questions(self, obj):
        return obj.get_questions()

    # TODO
    def get_progress(self, obj):
        return ""

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
            "submissions_count",
            "questions",
        )


class PracticeTestCreateSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField()

    # TODO
    def get_progress(self, obj):
        return ""

    class Meta:
        depth = 0
        model = PracticeTest
        fields = ("id", "test_id", "title", "instructions", "due_date", "subject", "created_by", "test_duration", "total_marks", "attachment", "progress")


class PracticeTestAnswerSubmissionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    answer = serializers.StringRelatedField()
    marks = serializers.SerializerMethodField()

    def get_marks(self, obj):
        return obj.question.marks if obj.answer.is_correct else 0

    class Meta:
        model = PracticeTestAnswerSubmission
        fields = ("id", "question", "answer", "marks")


class PracticeTestSubmissionListSerializer(serializers.ModelSerializer):
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
        model = PracticeTestSubmission
        fields = ("id", "test", "student", "student_id", "student_pk", "started_at", "marks_obtained", "grade_obtained", "answered_count")


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


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 0
        model = Standard
        fields = ("name", "code")


class SubjectSerializer(serializers.ModelSerializer):
    standard = serializers.StringRelatedField()
    total_students = serializers.SerializerMethodField()
    assignments = serializers.SerializerMethodField()
    class_tests = serializers.SerializerMethodField()
    performance = serializers.SerializerMethodField()
    syllabus_name = serializers.SerializerMethodField()

    def get_total_students(self, obj):
        return obj.get_students_count()

    # TODO
    def get_assignments(self, obj):
        return {"open": 10, "completed": 20, "pending": 30, "total": 60}

    # TODO
    def get_class_tests(self, obj):
        return {"open": 10, "completed": 20, "pending": 30, "total": 60}

    # TODO
    def get_performance(self, obj):
        return {"progress": 10, "avg_grade": "C", "class_avg": "30/50"}

    def get_syllabus_name(self, obj):
        return obj.syllabus.name

    class Meta:
        depth = 0
        model = Subject
        fields = ("id", "name", "syllabus", "syllabus_name", "code", "standard", "total_students", "assignments", "class_tests", "performance")


class ProgressCardTeacherSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        return obj.user.get_photo()

    class Meta:
        depth = 0
        model = Teacher
        fields = ("id", "user", "photo")


class SubjectProgressCardSerializer(serializers.ModelSerializer):
    assignments = serializers.SerializerMethodField()
    class_tests = serializers.SerializerMethodField()
    performance = serializers.SerializerMethodField()
    faculties = serializers.SerializerMethodField()
    mark = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()

    def get_faculties(self, obj):
        teachers = Teacher.objects.filter(subjects=obj)
        return ProgressCardTeacherSerializer(teachers, many=True).data

    # TODO
    def get_assignments(self, obj):
        return {"open": 10, "completed": 20, "pending": 30, "total": 60}

    # TODO
    def get_class_tests(self, obj):
        return {"open": 10, "completed": 20, "pending": 30, "total": 60}

    # TODO
    def get_performance(self, obj):
        return {"progress": 10, "avg_grade": "C", "class_avg": "30/50"}

    def get_mark(self, obj):
        return "30/50"

    def get_grade(self, obj):
        return "C"

    class Meta:
        depth = 0
        model = Subject
        fields = ("id", "name", "syllabus", "code", "faculties", "mark", "grade", "assignments", "class_tests", "performance")


class ProgressCardSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    standard = serializers.StringRelatedField()
    total_marks = serializers.SerializerMethodField()
    total_grade = serializers.SerializerMethodField()
    class_avg = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()

    def get_total_marks(self, obj):
        return "752/800"

    def get_total_grade(self, obj):
        return "A+"

    def get_class_avg(self, obj):
        return "600/800"

    def get_subjects(self, obj):
        return SubjectProgressCardSerializer(obj.standard.subjects.all(), many=True).data

    class Meta:
        depth = 0
        model = Student
        fields = ("student", "standard", "total_marks", "total_grade", "class_avg", "subjects")


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = ("creator", "user")

    def update(self, instance, validated_data):
        if "is_read" in validated_data:
            instance.is_read = validated_data["is_read"]
        instance.save()
        return instance


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
        instance.mock_answers.all().delete()
        for answer_data in answers_data:
            MockTestAnswer.objects.create(question=instance, **answer_data)
        return instance


class MockTestListSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    submissions_count = serializers.SerializerMethodField()

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    class Meta:
        depth = 0
        model = MockTest
        fields = ("id", "test_id", "title", "instructions", "created_by", "subject", "created_at", "test_duration", "total_marks", "attachment", "submissions_count")


class MockTestDetailSerializer(serializers.ModelSerializer):
    subject = serializers.StringRelatedField()
    subject_id = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    submissions_count = serializers.SerializerMethodField()
    questions = MockTestQuestionSerializer(many=True, source="mock_questions")

    def get_submissions_count(self, obj):
        return obj.get_submissions_count()

    def get_mock_questions(self, obj):
        return obj.get_questions()

    # TODO
    def get_progress(self, obj):
        return ""

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
            "submissions_count",
            "questions",
        )


class MockTestCreateSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()
    created_by = serializers.StringRelatedField()

    # TODO
    def get_progress(self, obj):
        return ""

    class Meta:
        depth = 0
        model = MockTest
        fields = ("id", "test_id", "title", "instructions", "subject", "created_by", "test_duration", "total_marks", "attachment", "progress")


class MockTestAnswerSubmissionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    answer = serializers.StringRelatedField()
    marks = serializers.SerializerMethodField()

    def get_marks(self, obj):
        return obj.question.marks if obj.answer.is_correct else 0

    class Meta:
        model = MockTestAnswerSubmission
        fields = ("id", "question", "answer", "marks")


class MockTestSubmissionListSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = MockTestSubmission
        fields = ("id", "test", "started_at", "marks_obtained", "grade_obtained", "answered_count")


class MockTestSubmissionDetailSerializer(serializers.ModelSerializer):
    test = serializers.StringRelatedField()
    marks_obtained = serializers.SerializerMethodField()
    grade_obtained = serializers.SerializerMethodField()
    answered_count = serializers.SerializerMethodField()
    answers = MockTestAnswerSubmissionSerializer(many=True, source="mock_answers")

    def get_marks_obtained(self, obj):
        return obj.marks_obtained()

    def get_grade_obtained(self, obj):
        return obj.grade_obtained()

    def get_answered_count(self, obj):
        return obj.answered_count()

    class Meta:
        depth = 1
        model = MockTestSubmission
        fields = ("id", "test", "started_at", "marks_obtained", "grade_obtained", "answered_count", "answers")
