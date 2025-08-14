# products/urls.py
from django.urls import path
from .views import SareeListAPIView

urlpatterns = [
    path('', SareeListAPIView.as_view(), name='saree-list'),
]
