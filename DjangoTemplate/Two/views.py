from django.http import HttpResponse
from django.shortcuts import render


def students(request):
    return HttpResponse("get students Success")


def student(request, s_id):
    print(s_id)
    print(type(s_id))
    return HttpResponse("Get One Student Success")


def get_time(request, hour, minute, second):
    return HttpResponse("Get Time IS %s: %s: %s" % (hour, minute, second))


def get_date(request, year, month, day):
    return HttpResponse("日付は %s - %s - %s" %(year, month, day))


def learn(request):
    return HttpResponse("love study")