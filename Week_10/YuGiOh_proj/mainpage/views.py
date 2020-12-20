from django.shortcuts import render
from django.views.generic import View, ListView, DetailView


def mainpage(request):
    context = {}
    return render(request, 'mainpage.html', context)

class CardDetailView(DetailView):
    model = Card
    template_name = 'card_list.html'
    fields = 

class CardListView(ListView):
    