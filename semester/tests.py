from django.test import TestCase
from rest_framework import status

from semester.models import Semester
from django.urls import reverse

from semester.serializers import SemesterSerializer


# class SemesterTestCase(TestCase):
#
#     def setUp(self):
#         self.semester = Semester.objects.create(term=0, year=2023)
#
#     def test_semester_list(self):
#         url = '/semesters/'
#         response = self.client.get(url)
#
#         for semester in response.data:
#             # Check that each semester object has 'term' and 'year' properties
#             self.assertIn('term', semester)
#             self.assertIn('year', semester)
#         print(response.data)
#
#     def test_semester_detail(self):
#         response = self.client.get(f'/semesters/{self.semester.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['term'], 0)
#         self.assertEqual(response.data['year'], 2023)
#         print(response.data)


class SemesterCreateListTestCase(TestCase):

    def setUp(self):
        self.semester_data = {'id': 1, 'term': 0, 'year': 2022}
        self.url = '/semesters/'

    def test_semester_list_create(self):
        # Test GET method
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # initially empty

        # Test POST method
        response = self.client.post(self.url, data=self.semester_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.semester_data)

        # Test GET method after creating a semester
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Test serializer
        semester = Semester.objects.get(id=1)
        serializer = SemesterSerializer(semester)
        self.assertEqual(response.data[0], serializer.data)
