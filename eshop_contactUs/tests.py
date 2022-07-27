from django.test import TestCase
from .models import Contact_us_model
class ContactUs_TestCase(TestCase):
    def setUp(self):
        Contact_us_model.objects.create(email="test@test.com",text="Test",full_name="TEST TEST",subject="tESt")
    def test_contact_us(self):
        form = Contact_us_model.objects.filter(text="Test").first()
        self.assertEqual(form.email,"test@test.com")
