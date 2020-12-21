from django.test import TestCase, SimpleTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from django.urls import reverse

chrome_webdriver = ChromeDriverManager().install()
# https://realpython.com/testing-in-django-part-1-best-practices-and-examples/


class MainpageTests(SimpleTestCase):
    def test_mainpage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('mainpage'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('mainpage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainpage.html')



class SeleniumBrowserSetupMixin:
    
    def _open_new_browser(self, headless=False):
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
        return webdriver.Chrome(executable_path=chrome_webdriver, options=options)

    def setUp(self):
        self.driver = self._open_new_browser()    
    def tearDown(self):
        self.driver.quit