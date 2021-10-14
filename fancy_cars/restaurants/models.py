from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        blank = False,
    )

    phone = models.CharField(
        max_length=200,
        blank = True,
    )

    address = models.CharField(
        max_length=200,
        blank = True,
    )

    city = models.CharField(
        max_length=200,
        blank = True,
    )

    state = models.CharField(
        max_length=10,
        blank = True,
    )

    zip_code = models.IntegerField(
        blank = True,
        default = 99999,
    )

    latitude = models.DecimalField(
        blank = True,
        max_digits=8,
        decimal_places=5,
    )

    longitude = models.DecimalField(
        blank = True,
        max_digits=10,
        decimal_places=6,
    )

    photo = models.ImageField(
        blank = True,
        upload_to = 'restaurantImages',
    )

    price = models.CharField(
        max_length=200,
        blank = True,
    )

    rating = models.DecimalField(
        blank = True,
        max_digits = 2,
        decimal_places = 1
    )

    def __str__(self):
        return self.name