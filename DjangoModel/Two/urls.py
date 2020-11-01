from django.conf.urls import url

from Two import views

urlpatterns = [
    url('getuser', views.get_user),
    url('gotusers', views.get_users),
    url('getorder', views.get_orders),
    url('getgrade', views.get_grade),
    url('getcustomer', views.get_customer),
    url('getcompany', views.get_company),
]
