from django.db.models import Max, F
from django.http import HttpResponse
from django.shortcuts import render

from Two.models import User, Order, Grade, Customer, Company, Animal


def get_user(request):
    username = "potter"
    password = "123"
    users = User.objects.filter(u_name=username)

    print(users.count())
    if users.exists():
        user = users.first()

        if user.u_password == password:
            print("succeed")
        else:
            print("wrong password")
    else:
        print("user isn't exit!")

    return HttpResponse("got it!")


def get_users(request):
    users = User.objects.all()[3:7]

    context = {
        "users": users,
    }
    return render(request, 'user_list.html', context=context)


def get_orders(request):
    orders = Order.objects.filter(o_time__month=9)
    for order in orders:
        print(order.o_num)
    return HttpResponse("got succeed")


def get_grade(request):
    # 根据 级联数据 查询
    grades = Grade.objects.filter(student__s_name='aa')
    for grade in grades:
        print(grade.s_name)

    return HttpResponse('okです')


def get_customer(request):
    result = Customer.objects.aggregate(Max('c_cost'))  # 一个字典类型
    print(result)

    return HttpResponse("cost succeed")


def get_company(request):
    companies = Company.objects.filter(c_boy_num__lt=F('c_girl_num'))
    for company in companies:
        print(company.c_name)
    return HttpResponse("company got succeed")


def get_animals(request):
    # animals = Animal.objects.all()
    # 使用自定义的 管理器 a_m
    # 方法已经重写
    animals = Animal.a_m.all()  # 此处 可将 a_m改为原来的objects（保持了源代码不变），在models里 将object名重赋值。。。。

    for animal in animals:
        print(animal.a_name)

    return HttpResponse("animal succeed")
