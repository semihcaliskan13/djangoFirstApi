from django.urls import path
from course.views import CourseDetail, CourseList


urlpatterns = [
    path('', CourseList.as_view()),
    path('<int:pk>/',CourseDetail.as_view())
]
