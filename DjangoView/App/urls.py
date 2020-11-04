from django.conf.urls import url

from App import views

urlpatterns = [
    url('hello', views.hello, name='hello'),
    url('getname', views.get_name, name='get_name'),
]