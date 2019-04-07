import json
from django.test import LiveServerTestCase
from django.urls import reverse

from store.endpoints import STORE
from api_auth.models import APIKey



class StoreAPITestCase(LiveServerTestCase):

  def setUp(self):
    self.PATH_POST = reverse(STORE.POST)
    key = str(APIKey.objects.create())
    self.headers = dict(HTTP_X_KEY=key)

  def post(self, data):
    return self.client.post(self.PATH_POST, data=data, content_type='application/json', **self.headers)
  
  def get(self, path):
    return self.client.get(path, follow=True, **self.headers)


  def test_post_endpoint_returns_url_to_object_if_valid_json_object_is_posted(self):
    data = dict(a=0)

    # test post
    res = self.post(data)
    self.assertEqual(res.status_code, 200)
    url = res.content.decode('utf-8')

    # test get
    res = self.get(url)
    self.assertEqual(res.status_code, 200)
    jsonStr = res.content.decode('utf-8')
    jsonObj = json.loads(jsonStr)
    
    self.assertEqual(data, jsonObj)


  def test_post_endpoint_returns_bad_request_if_invalid_json_is_posted(self):
    data = 'ajyaujq'

    res = self.post(data)
    self.assertEqual(res.status_code, 400)
  
  
  def test_get_endpoint_returns_http_method_not_allowed_if_key_not_passed(self):
    res = self.get(self.PATH_POST)
    self.assertEqual(res.status_code, 405)
  
  def test_get_endpoint_returns_http_not_found_if_key_does_not_exist(self):
    path = reverse(STORE.FETCH, kwargs=dict(id=10000))
    res = self.get(path)
    self.assertEqual(res.status_code, 404)