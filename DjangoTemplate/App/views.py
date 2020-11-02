from django.http import HttpResponse
from django.shortcuts import render

from App.models import Student


def hello(request):
    return HttpResponse('hello')


def index(request):
    return render(request, 'index.html')


def get_students(request):
    students = Student.objects.all().filter(s_name='harry')

    context = {
        "students": students,
    }
    return render(request, 'student_list.html', context=context)
