from django.test import TestCase
from users.models import CustomUser
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
       CustomUser.objects.create(username="test_user") 

    def test_get_user_model_returns_custom_user_class(self):
        custom_user = CustomUser.objects.get(username__iexact = "test_user")
        User = get_user_model()
        self.assertIsInstance(custom_user, User)
