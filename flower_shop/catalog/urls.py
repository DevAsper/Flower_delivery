from django.contrib import admin
from django.urls import path
from .views import product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('product/<int:id>/', product_detail, name='product_detail'),
]
