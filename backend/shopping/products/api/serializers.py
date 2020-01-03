from rest_framework import serializers
from products.models import Product,Offer

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','price','stock','image_url','value','productId')
        
