from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from main.models import Subject, Teacher
from web.models import AssignmentSubmission, ClassTest, MockTest, MockTestQuestion, MockTestSubmission, PracticeTest, TestQuestion, TestSubmission

from ..permissions import IsTeacher
from ..serializers import teacher as teacher_serializer


class TeacherProfileView(APIView):
    permission_classes = [IsTeacher]

    def get(self, request, format=None):
        teacher = Teacher.objects.get(user=request.user)
        serializer = teacher_serializer.TeacherSerializer(teacher)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.StudentListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ("standard", "student_id")
    search_fields = ["student_id", "user__first_name", "user__last_name", "user__email", "standard__name"]

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)
        return teacher_obj.get_students()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = teacher_serializer.StudentListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        student = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.StudentListSerializer(student, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def report(self, request, pk=None):
        student = get_object_or_404(self.get_queryset(), pk=pk)
        subject = request.query_params.get("subject")
        if not subject:
            return Response({"subject": "This field is required."}, status=400)
        serializer = teacher_serializer.ProgressCardSerializer(student, context={"request": request, "subject": subject})
        return Response(serializer.data)


class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.AssignmentDetailSerializer

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)
        return teacher_obj.get_assignments()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.AssignmentListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.AssignmentDetailSerializer(assignment, context={"request": request})
        return Response(serializer.data)

    def create(self, request):
        serializer = teacher_serializer.AssignmentCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            assignment = serializer.save(created_by=Teacher.objects.get(user=request.user))
            if "assigned_to" in request.data:
                assignment.assigned_to.clear()
                assignment.assigned_to.set(request.data["assigned_to"])
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.AssignmentCreateSerializer(assignment, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            if "assigned_to" in request.data:
                assignment.assigned_to.clear()
                assignment.assigned_to.set(request.data["assigned_to"])
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        assignment.delete()
        return Response(status=204)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        submissions = assignment.get_submissions()
        serializer = teacher_serializer.AssignmentSubmissionSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.AssignmentSubmissionSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return AssignmentSubmission.objects.filter(assignment__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.AssignmentSubmissionSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.AssignmentSubmissionSerializer(assignment, context={"request": request})
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.AssignmentSubmissionSerializer(assignment, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            # if marks is present in request data, update the submission to is_valuated = True
            if "marks" in request.data:
                serializer.save(is_valuated=True)
            else:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ClassTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.ClassTestListSerializer

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)
        return teacher_obj.get_class_tests()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.ClassTestListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.ClassTestDetailSerializer(class_test, context={"request": request})
        return Response(serializer.data)

    def create(self, request):
        serializer = teacher_serializer.ClassTestCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            class_test = serializer.save(created_by=Teacher.objects.get(user=request.user))
            if "assigned_to " in request.data:
                class_test.assigned_to.set(request.data["assigned_to"])
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.ClassTestCreateSerializer(class_test, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            if "assigned_to" in request.data:
                class_test.assigned_to.clear()
                class_test.assigned_to.set(request.data["assigned_to"])
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        class_test.delete()
        return Response(status=204)

    @action(detail=True, methods=["post"])
    def add_question(self, request, pk=None):
        class_test = get_object_or_404(ClassTest, pk=pk)
        serializer = teacher_serializer.ClassTestQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(test=class_test)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        submissions = class_test.get_submissions()
        serializer = teacher_serializer.TestSubmissionListSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)


class TestQuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.ClassTestQuestionSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return TestQuestion.objects.filter(test__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.ClassTestQuestionSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.ClassTestQuestionSerializer(question, context={"request": request})
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.ClassTestQuestionSerializer(question, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        question.delete()
        return Response(status=204)


class TestSubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.TestSubmissionListSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return TestSubmission.objects.filter(test__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.TestSubmissionListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        submission = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.TestSubmissionDetailSerializer(submission, context={"request": request})
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = Subject

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)
        return teacher_obj.get_classes()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.SubjectSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        subject = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.SubjectSerializer(subject, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        students = subject.get_students()
        serializer = teacher_serializer.StudentListSerializer(students, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def progress_cards(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        students = subject.get_students()
        serializer = teacher_serializer.StudentDetailSerializer(students, many=True, context={"request": request})
        return Response(serializer.data)


class PracticeTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.PracticeTestListSerializer

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)
        return teacher_obj.get_practice_tests()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.PracticeTestListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.PracticeTestDetailSerializer(practice_test, context={"request": request})
        return Response(serializer.data)

    def create(self, request):
        serializer = teacher_serializer.PracticeTestCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(created_by=Teacher.objects.get(user=request.user))
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.PracticeTestCreateSerializer(practice_test, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        practice_test.delete()
        return Response(status=204)

    @action(detail=True, methods=["post"])
    def add_question(self, request, pk=None):
        practice_test = get_object_or_404(PracticeTest, pk=pk)
        serializer = teacher_serializer.PracticeTestQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(test=practice_test)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        submissions = practice_test.get_submissions()
        serializer = teacher_serializer.PracticeTestSubmissionListSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)


class PracticeTestQuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.PracticeTestQuestionSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return TestQuestion.objects.filter(test__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.PracticeTestQuestionSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.PracticeTestQuestionSerializer(question, context={"request": request})
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.PracticeTestQuestionSerializer(question, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        question.delete()
        return Response(status=204)


class PracticeTestSubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.PracticeTestSubmissionListSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return TestSubmission.objects.filter(test__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.PracticeTestSubmissionListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        submission = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.PracticeTestSubmissionDetailSerializer(submission, context={"request": request})
        return Response(serializer.data)


# MockTest


class MockTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.MockTestListSerializer

    def get_queryset(self):
        teacher_obj = Teacher.objects.get(user=self.request.user)
        return teacher_obj.get_mock_tests()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.MockTestListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        mock_test = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.MockTestDetailSerializer(mock_test, context={"request": request})
        return Response(serializer.data)

    def create(self, request):
        serializer = teacher_serializer.MockTestCreateSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(created_by=Teacher.objects.get(user=request.user))
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        mock_test = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.MockTestCreateSerializer(mock_test, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        mock_test = get_object_or_404(queryset, pk=pk)
        mock_test.delete()
        return Response(status=204)

    @action(detail=True, methods=["post"])
    def add_question(self, request, pk=None):
        mock_test = get_object_or_404(MockTest, pk=pk)
        serializer = teacher_serializer.MockTestQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(test=mock_test)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        mock_test = get_object_or_404(queryset, pk=pk)
        submissions = mock_test.get_submissions()
        serializer = teacher_serializer.MockTestSubmissionListSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)


class MockTestQuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.MockTestQuestionSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return MockTestQuestion.objects.filter(test__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.MockTestQuestionSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.MockTestQuestionSerializer(question, context={"request": request})
        return Response(serializer.data)

    def update(self, request, pk=None, partial=False):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.MockTestQuestionSerializer(question, data=request.data, partial=partial, context={"request": request})
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        question = get_object_or_404(queryset, pk=pk)
        question.delete()
        return Response(status=204)


class MockTestSubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTeacher]
    serializer_class = teacher_serializer.MockTestSubmissionListSerializer

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return MockTestSubmission.objects.filter(test__created_by=teacher)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = teacher_serializer.MockTestSubmissionListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        submission = get_object_or_404(queryset, pk=pk)
        serializer = teacher_serializer.MockTestSubmissionDetailSerializer(submission, context={"request": request})
        return Response(serializer.data)
