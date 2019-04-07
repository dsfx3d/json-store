from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from api_auth.decorators import api_key_auth
from store.models import Json
from store.models.fields import DictField
from .responses import ErrorResponse, Response



@method_decorator(csrf_exempt, name="dispatch")
@method_decorator(api_key_auth, name="dispatch")
class StoreView (View):
  
  def post (self, request):
    jsonStr = request.body.decode('utf-8')

    try:
      entry = Json.objects.create(data=jsonStr)
    except DictField.InvalidJson as e:
      # return bad request
      return ErrorResponse.invalid_json(e)
    
    # return endpoint to fetch object
    return Response.object_url(request, entry)
  

  def get (self, request, *args, **kwargs):
    _id = kwargs.get('id')
    
    if _id is None:
      # list all request
      return ErrorResponse.method_list_not_allowed(request)
    
    try:
      entry = Json.objects.get(pk=_id)
    except Json.DoesNotExist:
      return ErrorResponse.not_found()

    return Response.json_object(entry)
