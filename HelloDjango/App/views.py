from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("Double click")


def second(request):
    return HttpResponse("返回的请求内容です。")


def third(request):
    return HttpResponse("<h1>这是Django的第二天</h2>")


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')
