import stripe

from django.db import models
from django.conf import settings

from users_app.models import Users

stripe.api_key = settings.STRIPE_SECRET_KEY

class ProductCategory(models.Model):
    name = models.CharField(max_length=125)
    descriptions = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
    image = models.ImageField(upload_to="product-image")
    stripe_product_price_id = models.CharField(max_length=128, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.category} --> {self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.stripe_product_price_id:
            stripe_product_price = self.create_stripe_product_price()
            self.stripe_product_price_id = stripe_product_price['id']
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def create_stripe_product_price(self):
        stripe_product = stripe.Product.create(name=self.name)
        stripe.Price.create(
            product=stripe_product,
            unit_amount=round(self.price*100),
            currency="uzs",
        )

class BasketsQuerySet(models.QuerySet):
    def get_total_quantity(self):
        return sum(basket.quantity for basket in self)

    def get_total_price(self):
        return sum(basket.get_price() for basket in self)

class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    creater_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketsQuerySet.as_manager()

    def __str__(self):
        return f"{self.user.username} uchun savatcha | Mahsulot: {self.product.name}, {self.quantity} dona"
    
    def get_price(self):
        return self.product.price*self.quantity