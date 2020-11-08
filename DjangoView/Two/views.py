import hashlib
from datetime import time
from random import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Two.models import Student


def hello(request):
    return HttpResponse('hello Two')


def login(request):
    if request.method == 'GET':
        return render(request, 'two_login.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        request.session["username"] = username
        return HttpResponse("success")


def mine(request):
    username = request.session.get("username")
    return HttpResponse(username)


def register(request):
    if request.method == "GET":
        return render(request, 'student_register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            student = Student()
            student.s_name = username
            student.s_password = password
            student.save()

        except Exception as e:
            return redirect(reverse("two:register"))

        return HttpResponse("success")


def student_login(request):
    if request.method == 'GET':
        render(request, 'student_login.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        students = Student.objects.filter(s_name=username).filter(s_password=password)
        if students.exists():
            student = students.first()
            ip = request.META.get("REMOTE_ADDR")
            token = generate_token(ip)
            student.s_token = token
            student.save()
            response = HttpResponse("login ok")
            response.set_cookie("token", token)
            return response
        return redirect(reverse("two: student_login"))


def generate_token(ip, username):
    c_time = time.ctime()
    r = username
    return hashlib.new("md5", (ip + c_time + r).encoder('utf-8')).hexdigest()


def student_mine(request):
    token = request.COOKIES.get('token')
    try:
        student = Student.objects.get(s_token=token)
    except Exception as e:
        return redirect("two: student_login")

    return HttpResponse(student.s_name)
