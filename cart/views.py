from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer



