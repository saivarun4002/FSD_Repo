# students/forms.py

from django import forms
from .models import StudentInfo, StudentMarks

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'mobile_number', 'hobbies']


class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = StudentMarks
        fields = ['name', 'marks']

