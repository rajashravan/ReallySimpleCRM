from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator


class Contact(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    address_line_1 = models.CharField(max_length=50, blank=True)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.PositiveIntegerField(
        null=True, blank=True, validators=[MaxValueValidator(999999)])
    profile_picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
