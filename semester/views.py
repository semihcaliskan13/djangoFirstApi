from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from djangoFirstApi.permissions import ReadOnly
from semester.models import Semester
from semester.serializers import SemesterSerializer


# Create your views here.


class SemesterList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # query_params içinden id ve name parametrelerini alın
        id = self.request.query_params.get('id', None)
        # name = self.request.query_params.get('name', None)

        # filtrelemeyi query_params'a göre yapın
        if id is not None:
            queryset = queryset.filter(id__gt=id)

        return queryset


class SemesterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
