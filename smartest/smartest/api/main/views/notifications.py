from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from main.models import Notification

from ..permissions import IsStudentOrTeacher
from ..serializers.teacher import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStudentOrTeacher]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = NotificationSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        notification = get_object_or_404(queryset, pk=pk)
        serializer = NotificationSerializer(notification, context={"request": request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        raise PermissionDenied("Deletion is disabled.")
