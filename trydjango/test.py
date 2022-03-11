import os
from  django.conf import settings
from django.test import TestCase

class TryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        #settings.SECRET_KEY
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        self.assertNotEqual(SECRET_KEY, 'abc123')