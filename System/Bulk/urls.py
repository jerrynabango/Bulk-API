from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ProductVariantListCreateAPIView,
    ProductVariantRetrieveUpdateDestroyAPIView,
    product_list,
)

urlpatterns = [
    path('Products/', product_list, name='product-list'),

    # Product URLs
    path('products/', ProductListCreateAPIView.as_view(),
         name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='product-detail'),

    # Product Variant URLs
    path('variants/', ProductVariantListCreateAPIView.as_view(),
         name='variant-list-create'),
    path('variants/<int:pk>/',
         ProductVariantRetrieveUpdateDestroyAPIView.as_view(),
         name='variant-detail'),
]
