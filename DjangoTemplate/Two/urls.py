from django.conf.urls import url

from Two import views

urlpatterns = [
    url('students/$', views.students),  # $结尾
    url('students/(\d+)/', views.student),
    url('gettime/(\d+)/(\d+)/(\d+)/', views.get_time),
    #url('getdate/(?p<year>\d+)/(?p<month>\d+)/(?p<day>\d+)/', views.get_date),
    url('getdate/(\d+)/(\d+)/(\d+)/', views.get_date),

    # url('learn/', views.learn, name='learn'),
]
