from django.urls import path
from .views import order_create, order_created, order_list, order_detail, change_order_status

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('created/<int:order_id>/', order_created, name='order_created'),
    path('admin/orders/<int:order_id>/', order_detail, name='order_detail'),
    path('admin/orders/<int:order_id>/status/<str:status>/', change_order_status, name='change_order_status'),
]
