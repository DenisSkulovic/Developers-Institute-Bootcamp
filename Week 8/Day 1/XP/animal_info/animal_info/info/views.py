from django.shortcuts import render
from info.models import Animal, Family



def family(request, id):
    family = Family.objects.get(id=id)
    animals = Animal.objects.filter(family=family)
    context = dict(family=family, animals=animals)
    return render(request, 'family.html', context)

def animal(request, id):
    animal = Animal.objects.get(id=id)
    context = dict(animal=animal)
    return render(request, "animal.html", context)

def animals(request):
    animals = Animal.objects.all()
    context = dict(animals=animals)
    return render(request, "animals.html", context)