# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse


# class SignupPageTests(TestCase):
#     username = 'testuser'
#     email = 'testuser@email.com'
#     def test_signup_page_status_code(self):
#         response = self.client.get('/account/signup/')
#         self.assertEqual(response.status_code, 200)
#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'signup.html')
#     def test_signup_form(self):
#         model = get_user_model()
#         test_user = model.objects.create_user(self.username, self.email)
#         self.assertEqual(model.objects.all().count(), 1)
#         self.assertEqual(model.objects.all()[0].username, self.username)
#         self.assertEqual(model.objects.all()[0].email, self.email)