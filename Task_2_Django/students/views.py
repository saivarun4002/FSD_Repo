# students/views.py

from django.shortcuts import render, redirect
from .forms import StudentInfoForm, StudentMarksForm

def student_info_view(request):
    if request.method == "POST":
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_info')  # Redirect to the same page or another URL
    else:
        form = StudentInfoForm()
    return render(request, 'students/student_info.html', {'form': form})


def student_marks_view(request):
    if request.method == "POST":
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_marks')
    else:
        form = StudentMarksForm()
    return render(request, 'students/student_marks.html', {'form': form})
