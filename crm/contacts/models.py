from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator

class Contact(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ) # note that this might be hard to set from the shell (should be automatic elsewhere)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True)
    address_line_1 = models.CharField(max_length=50, blank=True)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zipcode = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(999999)])
    # profile_picture = ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.first_name
