from django.contrib.auth.models import User
from django.test import TestCase

class Account_TestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Test",password="Test",email="test@test.com")
    def test_user(self):
        user = User.objects.filter(username="Test").first()
        self.assertEqual(user.email,"test@test.com")
