from django.conf.urls import url

from App import views

urlpatterns = [
    url('addpersons', views.add_persons),
    url('getpersons', views.get_persons),
    url('addperson', views.add_person),
    url('getperson', views.get_person),
]
