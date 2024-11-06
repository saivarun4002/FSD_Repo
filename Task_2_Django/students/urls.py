# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('student-info/', views.student_info_view, name='student_info'),
    path('student-marks/', views.student_marks_view, name='student_marks'),
]
