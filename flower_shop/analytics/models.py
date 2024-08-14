# apps/analytics/models.py
from django.db import models
from orders.models import Order

class Report(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Report for {self.date}'
