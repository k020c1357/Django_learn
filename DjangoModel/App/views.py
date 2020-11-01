import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):
    for i in range(20):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Mike%d" % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse("add persons succeed!")


def get_persons(request):
    persons = Person.objects.filter(p_age__gte=50).filter(p_age__lt=80).exclude(p_age=71)

    # print(type(persons)) # persons 可迭代
    context = {
        "persons": persons,
    }
    return render(request, 'person_list.html', context=context)


def add_person(request):
    # person = Person.objects.create(p_name="harry", p_age=25, p_sex=True) # 字段完整

    # "" 非 null None
    # person = Person(p_age=30)
    person = Person.create("Rhone")
    person.save()

    return HttpResponse("Harry,Rhone できた！")