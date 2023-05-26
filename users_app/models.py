from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class Users(AbstractUser):
    image = models.ImageField(upload_to="users_image", null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=True)

class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    expiration = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Verification object for {self.user.email_user}"

    def send_verification_email(self):
        link = reverse("users:verify", kwargs={"email": self.user.email, "code": self.code})
        verification_link = f"{settings.DOMAIN_NAME}{link}"
        subject = f"{self.user.email} uchun email manzilini tasdiqlash!"
        message = "foydalanuvchi {} ga email manzilini tasdiqlash uchun {} quyidagi havolaga o'ting".format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )
    def is_expired(self):
        return True if now() >= self.expiration  else False