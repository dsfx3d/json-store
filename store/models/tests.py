from django.test import TestCase

from . import Json
from .fields import DictField


class DictFieldTestCase(TestCase):

  def saveJson(self, data):
    return Json.objects.create(data=data)

  def assertInvalidJson(self, data):
    with self.assertRaises(DictField.InvalidJson):
      self.saveJson(data)

  def test_raises_exception_if_none_is_passed(self):
    self.assertInvalidJson(None)
  
  def test_raises_exception_if_empty_string_is_passed(self):
    self.assertInvalidJson('')

  def test_raises_exception_if_invalid_numerical_string_is_passed(self):
    self.assertInvalidJson('0.1')
    self.assertInvalidJson(1)
    self.assertInvalidJson('1')

  def test_raises_exception_if_invalid_json_string_is_passed(self):
    self.assertInvalidJson('{a:0}')

  def test_accepts_valid_json_string(self):
    value = '{"a":0}'
    obj = self.saveJson(value)
    self.assertEqual(value, str(obj))
  
  def test_accepts_dict(self):
    value = dict(a=0)
    obj = self.saveJson(value)
    self.assertEqual(value, obj.data)
  
  def test_always_returns_a_dict_if_saved_with_dict(self):
    val = dict(a=0)
    obj = self.saveJson(val)
    self.assertEqual(type(obj.data), dict)

  def test_always_returns_an_str_if_saved_with_str(self):
    val = '{"a":0}'
    obj = self.saveJson(val)
    self.assertEqual(type(obj.data), str)

  def test_method_from_db_value_always_returns_dict(self):
    obj = self.saveJson('{"a":0}')
    obj = Json.objects.get(pk=obj.id)
    self.assertEqual(type(obj.data), dict)