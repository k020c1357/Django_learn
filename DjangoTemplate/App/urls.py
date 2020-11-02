from django.conf.urls import url

from App import views

urlpatterns = [
    url('hello', views.hello),
    url('index', views.index),
    url('getstudents', views.get_students)
]