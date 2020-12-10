from django.shortcuts import render
from persons.models import Person

def phonenumber(response, phone_number):
    context = dict(person = Person.objects.get(phone_number = phone_number))
    return render(response, 'phonenumber.html', context)
    
    
def name(response, name):
    context = dict(person = Person.objects.get(name = name))
    return render(response, 'name.html', context)