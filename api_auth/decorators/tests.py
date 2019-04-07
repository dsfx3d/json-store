from django.test import TestCase, RequestFactory

from api_auth.models import APIKey
from .decorators import api_key_auth
from .enum import KEY


class ApiAuthDecoratorTestCase(TestCase):
  '''
  unit test decorators.api_key_auth
  '''
  
  def setUp(self):
    key_obj = APIKey.objects.create()
    self.key = key_obj.key

    inactive_key_obj = APIKey.objects.create(active=False)
    self.inactive_key = inactive_key_obj.key
    
    self.decor_func = api_key_auth(lambda x: True)
  
  class DummyRequest:
    def __init__(self, key=None):
      self.headers = {}
      self.headers[KEY] = key
  

  def assertBadRequest(self, request):
    res = self.decor_func(request)
    self.assertEqual(res.status_code, 400) # bad request
  
  def test_return_http_bad_request_if_api_key_is_missing(self):
    request = self.DummyRequest()
    request.headers.pop(KEY, None)
    self.assertBadRequest(request)

  def test_return_http_bad_request_if_api_key_does_not_exist(self):
    request = self.DummyRequest('akkajdsyys')
    self.assertBadRequest(request)

  def test_return_http_bad_request_if_api_key_is_inactive(self):
    request = self.DummyRequest(self.inactive_key)
    self.assertBadRequest(request)
  
  def test_execute_view_function_if_api_key_is_active(self):
    request = self.DummyRequest(self.key)
    view_func_called = self.decor_func(request)
    self.assertTrue(view_func_called)


