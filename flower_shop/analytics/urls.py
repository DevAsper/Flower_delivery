# apps/analytics/urls.py
from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('generate/', views.generate_report, name='generate_report'),
    path('dashboard/', views.analytics_dashboard, name='analytics_dashboard'),
]
