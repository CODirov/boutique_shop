from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products_app.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexView.as_view(), name="main-page"),
    path('products', include("products_app.urls")),
    path('users/', include("users_app.urls")),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
