from django.test import TestCase
from .models import SellOffer, BuyOffer
from django.utils import timezone
from django.core.urlsolvers import reverse
from django.contrib.auth import get_user_model
from mainpage.models import Card
from account.models import Profile
from django.contrib.auth import authenticate, login
# from .forms import 


# model tests
 
class OfferCreateTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='c0rrecth0rse',
        )
        self.buyoffer = BuyOffer.objects.create(
            card = Card.objects.get(id=1),
            price=12.34,
            profile = self.user.profile,
        )
        self.selloffer = SellOffer.objects.create(
            card = Card.objects.get(id=2),
            price=43.21,
            profile = self.user.profile,
        )
    def test_get_absolute_url(self):
        self.assertEqual(self.buyoffer.get_absolute_url(), 'buy/1/')
        self.assertEqual(self.selloffer.get_absolute_url(), 'sell/2/')

    def test_card(self):
        self.assertEqual(self.buyoffer.card, Card.objects.get(id=1))
        self.assertEqual(self.selloffer.card, Card.objects.get(id=2))

    def test_list_view(self):
        