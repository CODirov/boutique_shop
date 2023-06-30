from django.urls import path

from .views import OrderCreateView, CanceledTemplateView, SuccessTemplateView, OrderListView, OrderDetailView

app_name = "orders"

urlpatterns = [
    path("order-create", OrderCreateView.as_view(), name="order_create"),
    path("", OrderListView.as_view(), name="orders_list"),
    path("details/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("order-success/", SuccessTemplateView.as_view(), name="order_success"),
    path("order-canceled/", CanceledTemplateView.as_view(), name="order_canceled"),
]