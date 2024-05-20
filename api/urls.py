from django.urls import path
from .views import ProductListCreateAPIView, OrderListCreateAPIView, OrderDetailAPIView

urlpatterns = [
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
]
