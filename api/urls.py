from django.urls import path
from .views import ProductViewSet

urlpatterns = [
    path('', view=ProductViewSet.as_view({'post': 'create'})),
]