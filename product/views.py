
from rest_framework import generics
from .models import Sarees
from .serializers import ProductSerializer

class SareeListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Sarees.objects.filter(category='saree')
