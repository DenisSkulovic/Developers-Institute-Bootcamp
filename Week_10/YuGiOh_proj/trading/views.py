from django.shortcuts import render
from django.views.generic import View, ListView
from ygoprodeck import YGOPro
from mainpage.models import Type, Race, Archetype, Cardset, Image, CardPrice, Attribute, Card
from account.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from mainpage.db_functions import get_api_data, get_or_create, update_db
from django.contrib.auth.decorators import login_required
from trading.models import SellOffer, BuyOffer
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator





class Trading(View):
    def get(self, request):
        context = {}
        return render(request, 'trading.html', context)

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