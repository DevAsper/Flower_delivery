from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'status', 'paid', 'created', 'updated']
    list_filter = ['paid', 'status', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = ['mark_as_processed']

    def mark_as_processed(self, request, queryset):
        queryset.update(status='Processed')
    mark_as_processed.short_description = "Mark selected orders as Processed"
