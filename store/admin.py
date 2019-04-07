from django.contrib import admin

from .models import Json


class BaseModelAdmin(admin.ModelAdmin):
  filter = ('created_at', 'updated_at')


@admin.register(Json)
class JsonModelAdmin(BaseModelAdmin):
  list_display = ('data', 'created_at', 'updated_at',)
