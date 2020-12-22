from ygoprodeck import YGOPro
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (View, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView,
                                  TemplateView, )
from mainpage.models import (Type, Race, Archetype, 
                             Cardset, Image, CardPrice, 
                             Attribute, Card)
from db_functions import get_api_data, get_or_create, update_db
from trading.models import Offer
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

User = get_user_model()



class TradingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Offer
    template_name = 'trading_delete.html'
    success_url = reverse_lazy('trading_list')
    
    def test_func(self):
        if self.request.user.id == int(self.kwargs['pk']):
            return True
        else:
            return HttpResponse("<h1>You cannot delete other people's offers.</h1>")



class TradingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Offer
    template_name = 'trading_update.html'
    fields = ['card','price']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    def test_func(self):
        if self.request.user.id == int(self.kwargs['pk']):
            return True
        else:
            return HttpResponse("<h1>You cannot update other people's offers.</h1>")
    



class TradingDetailView(DetailView):
    model = Offer
    template_name = 'trading_detail.html'
    fields = '__all__'


class TradingListView(ListView):
    model = Offer
    template_name = 'trading_list.html'
    fields = '__all__'   
    
    
    
class TradingCreateView(LoginRequiredMixin, CreateView):
    model = Offer
    template_name = 'trading_create.html'
    fields = ['card','price']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
