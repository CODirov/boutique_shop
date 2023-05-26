from django.contrib import admin
from .models import Users

from products_app.admin import BasketAdmin
from .models import EmailVerification


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', "last_name")
    inlines = (BasketAdmin,)

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("code", "user", "expiration")
    readonly_fields = ("code", "user", "expiration")