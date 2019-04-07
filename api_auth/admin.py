from django.contrib import admin

from .models import APIKey


class BaseModelAdmin(admin.ModelAdmin):
  filter = ('created_at', 'updated_at')


@admin.register(APIKey)
class APIKeyModelAdmin(BaseModelAdmin):
  list_display = ('key', 'created_at', 'updated_at',)
  readonly_fields = ('key',)