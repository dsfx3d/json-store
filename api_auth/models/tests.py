from django.test import TestCase
from .models import APIKey


class APIKeyTestCase(TestCase):

  def setUp(self):
    self.key_obj = APIKey.objects.create()
  
  def test_str_of_object_always_return_key_value(self):
    self.assertEqual(str(self.key_obj), self.key_obj.key)