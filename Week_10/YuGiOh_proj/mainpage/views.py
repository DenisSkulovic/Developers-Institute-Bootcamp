from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import Card

def mainpage(request):
    context = {}
    return render(request, 'mainpage.html', context)

class CardDetailView(DetailView):
    model = Card
    template_name = 'card_detail.html'
    fields = ['name','type','desc','race','archetype','cardset','card_atk','card_def','card_level','attribute']

class CardListView(ListView):
    model = Card
    template_name = 'card_list.html'
    fields = ['name','type','desc','race','archetype','cardset','card_atk','card_def','card_level','attribute']
