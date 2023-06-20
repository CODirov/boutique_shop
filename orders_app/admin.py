from django.contrib import admin

from orders_app.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "status")
    readonly_fields = ("id", "created_at")