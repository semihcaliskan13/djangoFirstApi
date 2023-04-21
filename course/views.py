from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from course.models import Course
from course.serializers import CourseSerializer
from djangoFirstApi.permissions import ReadOnly


# Create your views here.

class CourseList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


