from django.db import models

from users_app.models import Users
from products_app.models import Basket

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

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        self.basket_history = {
            "purchased_items": [basket.de_json() for basket in baskets],
            "total_sum": float(baskets.get_total_price())
        }
        baskets.delete()
        self.save()