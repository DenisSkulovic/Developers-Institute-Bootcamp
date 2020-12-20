from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from ygoprodeck import YGOPro
from mainpage.models import Type, Race, Archetype, Cardset, Image, CardPrice, Attribute, Card
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from mainpage.db_functions import get_api_data, get_or_create, update_db
from django.contrib.auth.decorators import login_required
from trading.models import SellOffer, BuyOffer
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='get')
class TradingBuyUpdateView(UpdateView):
    model = BuyOffer
    template_name = 'trading_buy_update.html'
    fields = ['card','price']
    # make sure profile field is properly dealt with in views
    
@method_decorator(login_required, name='get')
class TradingSellUpdateView(UpdateView):
    model = SellOffer
    template_name = 'trading_sell_update.html'
    fields = ['card','price']
    # make sure profile field is properly dealt with in views

class TradingBuyDetailView(DetailView):
    model = BuyOffer
    template_name = 'trading_buy_detail.html'
    fields = '__all__'

class TradingSellDetailView(DetailView):
    model = SellOffer
    template_name = 'trading_sell_detail.html'
    fields = '__all__'

class TradingBuyListView(ListView):
    model = BuyOffer
    template_name = 'trading_buy_list.html'
    fields = '__all__'

class TradingSellListView(ListView):
    model = SellOffer
    template_name = 'trading_sell_list.html'
    fields = '__all__'
    
@method_decorator(login_required, name='get')
class TradingBuyCreateView(CreateView):
    model = BuyOffer
    template_name = 'trading_buy_create.html'
    fields = ['card','price']
    # make sure profile field is properly dealt with in views

@method_decorator(login_required, name='get')
class TradingSellCreateView(CreateView):
    model = SellOffer
    template_name = 'trading_sell_create.html'
    fields = ['card','price']
    # make sure profile field is properly dealt with in views

class Trading(View):
    def get(self, request):
        context = {}
        return render(request, 'trading.html', context)




# everything below is cringy garbage
class SellOfferViewAll(View):
    def get(self, request, page):
        all_cards = SellOffer.objects.all()
        if all_cards:
            paginator = Paginator(all_cards, 10)
            page_obj = paginator.get_page(page)
            context = {
                'page_obj': page_obj,
            }
        else:
            context = {'page_obj': None}
        return render(request, 'trading_sell_all.html', context) 


class BuyOfferViewAll(View):
    def get(self, request, page):
        all_cards = SellOffer.objects.all()
        paginator = Paginator(all_cards, 10)
        page_obj = paginator.get_page(page)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'trading_buy_all.html', context)
    
    
@method_decorator(login_required, name='get')  
class SellOfferView(View):
    def get(self, request, page):
        profile = Profile.objects.get(user=request.user)
        profile_cards = profile.cards
        all_cards_for_sale = SellOffer.objects.all()
        
        view_cards = set(all_cards_for_sale).intersection(set(profile_cards))
        
        paginator = Paginator(list(view_cards), 10)
        page_obj = paginator.get_page(page)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'trading_sell.html', context)
    
    
@method_decorator(login_required, name='get')
class BuyOfferView(View):
    def get(self, request, page):
        profile = Profile.objects.get(user=request.user)
        profile_cards = profile.cards
        all_cards_for_buy = BuyOffer.objects.all()
        
        view_cards = set(all_cards_for_buy).intersection(set(profile_cards))
        
        paginator = Paginator(list(view_cards), 10)
        page_obj = paginator.get_page(page)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'trading_buy.html', context)