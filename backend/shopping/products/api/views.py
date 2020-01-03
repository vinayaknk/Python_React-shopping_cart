from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView
from products.models import Product
from .serializers import productSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer