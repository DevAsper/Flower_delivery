# apps/reviews/urls.py
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('product/<int:product_id>/reviews/', views.product_reviews, name='product_reviews'),
]
