from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import RecipeIngredient, Recipe

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('punith.mk', password='1234')
        
    def test_user_pw(self):
        checked = self.user_a.check_password("1234")
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('punith.mk', password='1234')

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)
    
    def test_user_recipe_count(self):
        