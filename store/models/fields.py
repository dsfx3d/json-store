import json
from django.db import models


class DictField (models.TextField):
  '''
  @accept dict or valid json string
  @return json
  '''
  ERR_INVALID_JSON = 'not a valid json'
  
  class InvalidJson(ValueError):
    pass


  def get_prep_value(self, value):
    '''
    validate and convert to string if required, before saving to db
    '''
    try:
      if isinstance(value, dict):
        return json.dumps(value)
      elif isinstance(value, str):
        v = json.loads(value)
        if not isinstance(v, dict):
          raise ValueError
        return json.dumps(v)
    except:
      pass
    
    raise self.InvalidJson(self.ERR_INVALID_JSON)

  
  def to_python(self, value):
    return json.loads(value)
  

  def from_db_value(self, value, *args):
    return self.to_python(value)