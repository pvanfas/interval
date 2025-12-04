from core.models import About
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AboutSerializer
from .serializers import CourseEnquirySerializer
from .serializers import CreateContactSerializer
from .serializers import ProductEnquirySerializer


class AboutView(RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.last()


class CreateContact(APIView):
    def post(self, request, format=None):
        serializer = CreateContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductEnquiry(APIView):
    def post(self, request, format=None):
        serializer = ProductEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseEnquiry(APIView):
    def post(self, request, format=None):
        serializer = CourseEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
