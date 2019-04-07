from api_auth.models import APIKey
from . import response
from .enum import KEY

def api_key_auth(function):
  def wrap(request, *args, **kwargs):
    api_key = request.headers.get(KEY)

    if api_key is None:
      return response.error(f'add api key in `{KEY}` request header')

    try:
      key_obj = APIKey.objects.get(key=api_key)
      if key_obj.active is False:
        return response.error('unauthorized api key')
    except APIKey.DoesNotExist:
      return response.error('api key does not exist')

    return function(request, *args, **kwargs)
  
  return wrap
  