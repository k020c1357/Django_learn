from django.conf.urls import url

from App import views

urlpatterns = [
    url('hello', views.hello, name='hello'),
    url('getname', views.get_name, name='get_name'),
    url('getinfo', views.get_info, name='get_info'),
    url('setcookie', views.set_cookie,name='set_cookie'),
    url('getcookie', views.get_cookie, name='get_cookie'),
]