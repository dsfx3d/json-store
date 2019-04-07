from urllib.parse import urljoin
from django.urls import reverse
from django.http import HttpResponse, JsonResponse

from store.endpoints import STORE


class ErrorResponse:

  @staticmethod
  def error(e, status=400):
    res = dict(error=e)
    return JsonResponse(res, status=status)
  
  @classmethod
  def method_list_not_allowed (cls, request, status=405):
    valid_path = reverse(STORE.FETCH, kwargs=dict(id='your_object_key'))
    valid_url = urljoin(request.build_absolute_uri('/'), valid_path)
    return cls.error(f'request GET { valid_url } to fetch your json object', status=status)

  @classmethod
  def invalid_json(cls, e, status=400):
    return cls.error(str(e), status=status)
  
  @classmethod
  def not_found(cls, status=404):
    return cls.error('Not Found. Try with valid key',status=status)


class Response:
  
  @staticmethod
  def object_url (request, entry):
    url = request.build_absolute_uri('/')
    url = urljoin(url, reverse(STORE.POST) + str(entry.id)),
    return HttpResponse(url)
  
  @staticmethod
  def json_object (entry):
    return JsonResponse(entry.data)