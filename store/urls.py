from django.urls import path

from .views import StoreView
from .endpoints import STORE

urlpatterns = [
  path('store/', StoreView.as_view(), name=STORE.POST),
  path('store/<str:id>/', StoreView.as_view(), name=STORE.FETCH)
]