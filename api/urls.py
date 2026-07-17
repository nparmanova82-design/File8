from django.urls import path
from .views import (CreateProductView,ProductListAPIView,ProductRetrieveAPIView,ProductUpdateAPIView,ProductDestroyAPIView,ProductRetrieveUpdateAPIView,)

urlpatterns = [
    path("products/create/", CreateProductView.as_view(), name="product-create"),
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product-detail"),
    path("products/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDestroyAPIView.as_view(), name="product-delete"),
    path("products/<int:pk>/detail-update/",ProductRetrieveUpdateAPIView.as_view(),name="product-detail-update",
    ),
]