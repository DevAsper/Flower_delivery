# apps/analytics/views.py
from django.shortcuts import render
from django.db.models import Sum, F
from orders.models import Order
from .models import Report
import datetime

def generate_report(request):
    today = datetime.date.today()
    report, created = Report.objects.get_or_create(date=today)

    if created:
        # Рассчитываем общие продажи, прибыль и расходы за сегодня
        total_sales = Order.objects.filter(order_date__date=today).aggregate(
            total=Sum(F('items__product__price') * F('items__quantity'))
        )['total'] or 0

        total_profit = total_sales * 0.3  # Пример расчета прибыли как 30% от продаж
        total_expenses = total_sales * 0.7  # Пример расчета расходов как 70% от продаж

        report.total_sales = total_sales
        report.total_profit = total_profit
        report.total_expenses = total_expenses
        report.save()

    return render(request, 'analytics/report.html', {'report': report})

def analytics_dashboard(request):
    reports = Report.objects.all().order_by('-date')
    return render(request, 'analytics/dashboard.html', {'reports': reports})
