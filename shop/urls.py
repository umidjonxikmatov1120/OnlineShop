from django.urls import path

from shop.views import ProductsListCreateView, ProductsReadUpdateDeleteView, ProductsListView

urlpatterns = [
    path('', ProductsListView.as_view()),
    path('products/create', ProductsListCreateView.as_view()),
    path('products/<int:pk>/', ProductsReadUpdateDeleteView.as_view())
]


