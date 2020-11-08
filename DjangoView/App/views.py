import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse


def hello(request):
    # HttpResponse 的属性
    response = HttpResponse()
    # response.content = 'hello Django!'
    # response.status_code = 404
    # HttpResponse 方法
    response.write("nice to meet you!")
    response.flush()  # 清除缓冲区
    return response


def get_name(request):
    # if random.randrange(10) > 5:   重定向
    #   return HttpResponseRedirect('/app/hello/')
    url = reverse('App:hello')
    return HttpResponseRedirect(url)


def get_info(request):
    data = {
        "status": 200,
        "msg": 'ok',
    }
    return JsonResponse(data=data)


def set_cookie(request):
    response = HttpResponse("set cookies")
    response.set_cookie('username', 'okinawa')
    return response


def get_cookie(request):
    username = request.COOKIES.get('username')
    return HttpResponse(username)