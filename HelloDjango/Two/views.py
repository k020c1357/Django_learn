import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Student


def index(request):
    return HttpResponse("Two index")


def add_student(request):
    student = Student()
    student.s_name = "Jerry%d" % random.randrange(100)
    student.save()
    return HttpResponse("ADD success %s" % student.s_name)


def get_students(request):
    students = Student.objects.all()
    for student in students:
        print(student.s_name)
    # return HttpResponse("Students List")
    context = {
        "hobby": "play games",
        "eat": "ラーメン",
        "students": students,
    }
    return render(request, 'student_list.html', context=context)


def update_student(request):
    student = Student.objects.get(pk=2)
    student.s_name = "Tom"
    student.save()

    return HttpResponse("student update succeed!")


def delete_student(request):

    student = Student.objects.get(pk= 3)
    student.delete()

    return HttpResponse("student delete succeed!")
