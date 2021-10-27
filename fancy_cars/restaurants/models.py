from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_review = models.CharField(
        max_length = 100,
        unique = True,
    )
    active = models.BooleanField(
        default = True,
    )

    def __str__(self):
        return str(self.tag_review)


class Restaurant(models.Model):
    name = models.CharField(
        max_length=200,
        blank = False,
    )

    tag = models.ManyToManyField(
        Tag, 
        blank = True
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
        default = 0.0,
    )

    longitude = models.DecimalField(
        blank = True,
        max_digits=10,
        decimal_places=6,
        default = 0.0
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
        decimal_places = 1,
    )

    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )

    review = models.TextField(
        blank = False,
    )

    user_rating = models.DecimalField(
        blank = True,
        max_digits = 2,
        decimal_places = 1
    )
    
    def __str__(self):
        return self.review

