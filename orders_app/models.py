from django.db import models

from users_app.models import Users

class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, "Qo'shildi"),
        (PAID, "To'landi"),
        (ON_WAY, "Yo'lda"),
        (DELIVERED, "Yetkazildi"),
    )

    first_name = models.CharField(max_length=77)
    last_name = models.CharField(max_length=77)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    basket_history = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"order #{self.id}, {self.first_name}, {self.last_name}"