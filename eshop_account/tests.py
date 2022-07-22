from django.contrib.auth.models import User
from django.test import TestCase

class Account_TestCase(TestCase):
    def setUp(self):
        u = User.objects.create(username="Test",password="Test",email="test@test.com")
        u.reset_password.reset_code = 56544
    def test_user(self):
        user = User.objects.filter(username="Test",reset_password__is_baned=False).first()
        self.assertEqual(user.email,"test@test.com")
        self.assertEqual(user.reset_password.is_baned,False)
        self.assertFalse(user.reset_password is None)

class home_page_test(TestCase):
    def test_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code ,200)
