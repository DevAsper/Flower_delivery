# apps/reports/models.py
from django.db import models
from orders.models import Order

class Report(models.Model):
    report_date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='reports')
    sales_data = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Report {self.id} - {self.report_date}'
