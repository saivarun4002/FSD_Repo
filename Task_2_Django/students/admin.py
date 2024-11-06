# students/admin.py

from django.contrib import admin
from .models import StudentInfo, StudentMarks

admin.site.register(StudentInfo)
admin.site.register(StudentMarks)
