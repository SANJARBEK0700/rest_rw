from django.urls import path
from .views import get_info, create_product, list_product, detail_product, update_product, patch_product
urlpatterns = [
    path('get_info/', get_info),
    path('create_product/', create_product),
    path('list/', list_product),
    path('prod/<int:pk>/', detail_product),
    path('update/<int:pk>/', update_product),
    path('patch/<int:pk>/', patch_product),
]