from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products_app.views import IndexView
from orders_app.views import stripe_webhook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="main-page"),
    path('products/', include("products_app.urls")),
    path('users/', include("users_app.urls")),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders_app.urls')),
    path('webhook/stripe/', stripe_webhook_view, name="stripe_webhook"),
]
if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
