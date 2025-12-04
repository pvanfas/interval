from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Student, Syllabus
from web.models import Assignment, AssignmentSubmission, ClassTest, Event, MockTest, MockTestSubmission, PracticeTest, PracticeTestSubmission, TestSubmission

from ..permissions import IsStudent
from ..serializers import student as student_serializer
from ..serializers.teacher import ProgressCardSerializer


class SyllabusListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        syllabus = Syllabus.objects.all()
        serializer = student_serializer.SyllabusSerializer(syllabus, many=True)
        return Response(serializer.data)


class StudentProfileView(APIView):
    permission_classes = [IsStudent]

    def get(self, request, format=None):
        student_obj = Student.objects.get(user=request.user)
        serializer = student_serializer.StudenProfileSerializer(student_obj, context={"request": request})
        return Response(serializer.data)


class StudentUpcomingView(APIView):
    permission_classes = [IsStudent]

    def get(self, request, format=None):
        student_obj = Student.objects.get(user=request.user)
        upcoming_tests = ClassTest.objects.filter(assigned_to=student_obj, is_active=True)[:5]
        upcoming_assignments = Assignment.objects.filter(assigned_to=student_obj, is_active=True)[:5]
        upcoming_events = Event.objects.filter(date__gte=timezone.now(), is_active=True)[:5]
        return Response(
            {
                "upcoming_tests": student_serializer.ClassTestListSerializer(upcoming_tests, many=True, context={"request": request}).data,
                "upcoming_assignments": student_serializer.AssignmentDetailSerializer(upcoming_assignments, many=True, context={"request": request}).data,
                "upcoming_events": student_serializer.EventSerializer(upcoming_events, many=True, context={"request": request}).data,
            }
        )


class StudentProgressCardView(APIView):
    permission_classes = [IsStudent]

    def get(self, request, pk=None):
        student = Student.objects.get(user=request.user)
        subject = student.standard
        serializer = ProgressCardSerializer(student, context={"request": request, "subject": subject})
        return Response(serializer.data)


class ClassTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStudent]
    serializer_class = student_serializer.ClassTestListSerializer

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        return ClassTest.objects.filter(assigned_to=student)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = student_serializer.ClassTestListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        serializer = student_serializer.ClassTestDetailSerializer(class_test, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        submissions = TestSubmission.objects.filter(test=class_test, student=request.user.student)
        serializer = student_serializer.TestSubmissionListSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def submit(self, request, pk=None):
        queryset = self.get_queryset()
        class_test = get_object_or_404(queryset, pk=pk)
        submission_obj, _ = TestSubmission.objects.get_or_create(test=class_test, student=request.user.student)
        if submission_obj.is_completed:
            raise PermissionDenied("You have already submitted this test.")
        serializer = student_serializer.TestAnswerSubmissionSerializer(submission_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(submission=submission_obj)
        return Response(serializer.data)


class AssignmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStudent]
    serializer_class = student_serializer.AssignmentDetailSerializer

    def get_queryset(self):
        student = Student.objects.get(user=self.request.user)
        return Assignment.objects.filter(assigned_to=student)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = student_serializer.AssignmentDetailSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        serializer = student_serializer.AssignmentDetailSerializer(assignment, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        submissions = AssignmentSubmission.objects.filter(assignment=assignment, student=request.user.student)
        serializer = student_serializer.AssignmentSubmissionSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def submit(self, request, pk=None):
        queryset = self.get_queryset()
        assignment = get_object_or_404(queryset, pk=pk)
        submission = AssignmentSubmission.objects.filter(assignment=assignment, student=request.user.student).first()
        if submission:
            raise PermissionDenied("You have already submitted this assignment.")
        serializer = student_serializer.AssignmentSubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(assignment=assignment, student=request.user.student)
        return Response(serializer.data)


class EventViewset(viewsets.ViewSet):
    permission_classes = [IsStudent]

    def list(self, request):
        events = Event.objects.filter(date__gte=timezone.now(), is_active=True)
        serializer = student_serializer.EventSerializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = student_serializer.EventSerializer(event)
        return Response(serializer.data)


class PracticeTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStudent]
    serializer_class = student_serializer.PracticeTestListSerializer

    def get_queryset(self):
        student_obj = Student.objects.get(user=self.request.user)
        return PracticeTest.objects.filter(subject__standard=student_obj.standard)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = student_serializer.PracticeTestListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        serializer = student_serializer.PracticeTestDetailSerializer(practice_test, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        submissions = practice_test.get_submissions()
        serializer = student_serializer.PracticeTestSubmissionListSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def submit(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        submission_obj, _ = PracticeTestSubmission.objects.get_or_create(test=practice_test, student=request.user.student)
        serializer = student_serializer.PracticeTestAnswerSubmissionSerializer(submission_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(submission=submission_obj)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def report(self, request, pk=None):
        queryset = self.get_queryset()
        practice_test = get_object_or_404(queryset, pk=pk)
        submission_obj, _ = PracticeTestSubmission.objects.get_or_create(test=practice_test, student=request.user.student)
        serializer = student_serializer.PracticeResultSerializer(submission_obj, context={"request": request})
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStudent]
    serializer_class = student_serializer.SubjectSerializer

    def get_queryset(self):
        student_obj = Student.objects.get(user=self.request.user)
        return student_obj.standard.subjects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = student_serializer.SubjectSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        subject = get_object_or_404(queryset, pk=pk)
        serializer = student_serializer.SubjectSerializer(subject, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def assignments(self, request, pk=None):
        queryset = self.get_queryset()
        subject = get_object_or_404(queryset, pk=pk)
        assignments = Assignment.objects.filter(assigned_to=request.user.student, subject=subject)
        serializer = student_serializer.AssignmentDetailSerializer(assignments, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def tests(self, request, pk=None):
        queryset = self.get_queryset()
        subject = get_object_or_404(queryset, pk=pk)
        tests = ClassTest.objects.filter(assigned_to=request.user.student, subject=subject)
        serializer = student_serializer.ClassTestListSerializer(tests, many=True, context={"request": request})
        return Response(serializer.data)


class MockTestViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = student_serializer.MockTestListSerializer

    def get_queryset(self):
        return MockTest.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = student_serializer.MockTestListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        mock_test = get_object_or_404(queryset, pk=pk)
        serializer = student_serializer.MockTestDetailSerializer(mock_test, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def submissions(self, request, pk=None):
        queryset = self.get_queryset()
        mock_test = get_object_or_404(queryset, pk=pk)
        submissions = mock_test.get_submissions()
        serializer = student_serializer.MockTestSubmissionListSerializer(submissions, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def submit(self, request, pk=None):
        submission_obj, _ = MockTestSubmission.objects.get_or_create(pk=pk)
        serializer = student_serializer.MockTestAnswerSubmissionSerializer(submission_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(submission=submission_obj)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def report(self, request, pk=None):
        submission_obj, _ = MockTestSubmission.objects.get_or_create(pk=pk)
        serializer = student_serializer.MockResultSerializer(submission_obj, context={"request": request})
        return Response(serializer.data)


class MockTestSubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = student_serializer.MockTestSubmissionStartSerializer

    def get_queryset(self):
        return MockTestSubmission.objects.all()

    def create(self, request):
        serializer = student_serializer.MockTestSubmissionStartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not request.session.session_key:
            request.session.create()

        test_instance = MockTest.objects.get(id=request.data["test_id"])
        if MockTestSubmission.objects.filter(session_id=request.session.session_key, test=test_instance).exists():
            serializer = student_serializer.MockTestSubmissionStartSerializer(MockTestSubmission.objects.get(session_id=request.session.session_key, test=test_instance))
        else:
            serializer.save(session_id=request.session.session_key, test=test_instance)
        return Response(serializer.data)
