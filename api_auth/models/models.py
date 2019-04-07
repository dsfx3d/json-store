from django.db import models

from .utils import generateApiKey
from . import API_KEY_LEN



class BaseModel(models.Model):
  class Meta:
    abstract = True

  created_at = models.DateTimeField(verbose_name='createdAt', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updatedAt', auto_now=True)



class APIKey(BaseModel):
  '''
  to authorize api requests
  '''

  key = models.CharField(max_length=API_KEY_LEN, default=generateApiKey)
  active = models.BooleanField(verbose_name='isActive', default=True)

  def __str__(self):
    return self.key

  class Meta:
    verbose_name = 'Key'
    verbose_name_plural = 'Keys'
