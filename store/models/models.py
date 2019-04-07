from django.db import models
from .fields import DictField


class BaseModel(models.Model):
  class Meta:
    abstract = True

  created_at = models.DateTimeField(verbose_name='createdAt', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='updatedAt', auto_now=True)


class Json(BaseModel):
  '''
  To store json objects
  '''
  data = DictField()

  def __str__(self):
    return self.data

  class Meta:
    verbose_name = 'JSON'
    verbose_name_plural = 'JSON'
