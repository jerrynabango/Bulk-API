from django.shortcuts import render
from rest_framework import generics
from .models import Product, ProductVariant
from .serializers import ProductSerializer, ProductVariantSerializer


# List and Create Products
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Retrieve, Update, and Delete a Product
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# List and Create Product Variants
class ProductVariantListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


# Retrieve, Update, and Delete a Product Variant
class ProductVariantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


def product_list(request):
    products = Product.objects.prefetch_related('variants').all()
    return render(request, 'products.html', {'products': products})
