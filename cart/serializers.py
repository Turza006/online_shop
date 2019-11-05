from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('buyer_id','product_id','quantity','seller_id')



