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
    persons = Person.objects.filter(p_age__gte=20)
    context = {
        "persons": persons,
    }
    return render(request, 'person_list.html', context=context)
