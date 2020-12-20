from django.test import TestCase
from .models import SellOffer, BuyOffer
from django.utils import timezone
from django.core.urlsolvers import reverse
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from .forms import 


# https://realpython.com/testing-in-django-part-1-best-practices-and-examples/


# model tests
def open_new_browser(headless=False):
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    if headless == True:
        options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--use-gl=desktop')
    options.add_argument('--log-level=3')
    options.add_argument("--disable-extensions")
    # options.add_argument("--incognito")
    return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

class SimpleBrowserSetupMixin:
    def setUp(self):
        self.driver = open_new_browser()    
    def tearDown(self):
        self.driver.quit
 
class OfferCreateTest(SimpleBrowserSetupMixin, TestCase):
    def test_trading_sell_create(self):
        self.driver.get('http://localhost:8000/UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED-submit').click()
    def test_trading_buy_create(self):
        self.driver.get('http://localhost:8000/UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED-submit').click()


class OfferUpdateTest(SimpleBrowserSetupMixin, TestCase):
    def test_trading_sell_update(self):
        self.driver.get('http://localhost:8000/UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED-submit').click()
    def test_trading_buy_update(self):
        self.driver.get('http://localhost:8000/UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED').send_keys('UNFINISHED')
        self.driver.find_element_by_id('UNFINISHED-submit').click()


# form tests
# this obviously needs a class like above
class UNFINISHEDFormTest(SimpleBrowserSetupMixin, TestCase):
    def test_sell_offer_valid_from(self):
        selloffer = SellOffer.objects.create(UNFINISHED1='UNFINISHED', UNFINISHED2 = 'UNFINISHED')
        data = {'UNFINISHED1': selloffer.UNFINISHED1, 'UNFINISHED2':selloffer.UNFINISHED2}
        form = UNFINISHEDform(data=data)
        self.assertTrue(form.is_valid())
    def test_sell_offer_invalid_from(self):
        selloffer = SellOffer.objects.create(UNFINISHED1='UNFINISHED', UNFINISHED2 = '')
        data = {'UNFINISHED1': selloffer.UNFINISHED1, 'UNFINISHED2':selloffer.UNFINISHED2}
        form = UNFINISHEDform(data=data)
        self.assertFalse(form.is_valid())


