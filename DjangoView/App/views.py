import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def hello(request):
    # HttpResponse 的属性
    response = HttpResponse()
    # response.content = 'hello Django!'
    # response.status_code = 404
    # HttpResponse 方法
    response.write("nice to meet you!")
    response.flush()   # 清除缓冲区
    return response


def get_name(request):
    if random.randrange(10) > 5:
        return HttpResponseRedirect('/app/hello/')
    return HttpResponse("all right!")
