from django.conf.urls import url

from Two import views

urlpatterns = {
    url('hello/', views.hello, name='hello'),
    url('login/', views.login, name='login'),
    url('mine/', views.mine, name='mine'),
    url('register/', views.register, name='register'),
    url('studentlogin/', views.student_login, name='studentlogin'),
    url('studentmine/', views.student_mine, name='studentmine'),
}
