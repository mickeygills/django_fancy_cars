from django.db import models
from django.urls import reverse

# Create your models here.
class Cars(models.Model):

## Make Options
    ASTON_MARTIN = 'Aston Martin'   
    BENTLEY = 'Bentley'    
    BUGATTI = 'Bugatti'
    FERRARI = 'Ferrari'
    PAGANI = 'Pagani'
    LAMBORGHINI = 'Lamborghini'
    MCLAREN = 'McLaren'
    MERCEDES_AMG = 'Mercedes AMG'
    MERCEDES_MAYBACH = 'Mercedes-Maybach'
    PININFARINA = 'Pininfarina'
    ROLLS_ROYCE = 'Rolls Royce'
    W_MOTORS = 'W Motors'
    MAKE_OPTIONS = [
        (ASTON_MARTIN, 'Aston Martin'),
        (BENTLEY, 'Bentley'),
        (BUGATTI, 'Bugatti'),
        (FERRARI, 'Ferrari'),
        (PAGANI, 'Pagani'),
        (LAMBORGHINI, 'Lamborghini'),
        (MCLAREN, 'McLaren'),
        (MERCEDES_AMG, 'Mercedes AMG'),
        (MERCEDES_MAYBACH, 'Mercedes-Maybach'),
        (PININFARINA, 'Pininfarina'),
        (ROLLS_ROYCE, 'Rolls Royce'),
        (W_MOTORS, 'W Motors'),
    ]
    make = models.CharField(
        choices = MAKE_OPTIONS,
        max_length = 100,
        )

    model = models.CharField(
        max_length = 100,
        blank = False,
    )

    price = models.DecimalField(
        max_digits = 4,
        decimal_places = 2,
        blank = False,
    )

## Color Options
    WHITE_METALLIC = 'White Metallic'
    BLACK = 'Black'
    GRAY = 'Gray'
    BLUE_AND_SILVER = 'Blue and Silver'
    RED = 'Red'
    GOLD_AND_GREEN = 'Gold and Green'
    BROWN = 'Brown'
    ORANGE = 'Orange'
    COLOR_OPTIONS = [
        (WHITE_METALLIC, 'White Metallic'),
        (BLACK, 'Black'),
        (GRAY, 'Gray'),
        (BLUE_AND_SILVER, 'Blue and Silver'),
        (RED, 'Red'),
        (GOLD_AND_GREEN, 'Gold and Green'),
        (BROWN, 'Brown'),
        (ORANGE, 'Orange'),
    ]
    color = models.CharField(
        choices = COLOR_OPTIONS,
        max_length = 100,
        )

## Year Options
    x2017 = '2017'
    x2018 = '2018'
    x2019 = '2019'
    x2020 = '2020'
    x2021 = '2021'
    YEAR_OPTIONS = [
        (x2017, '2017'),
        (x2018, '2018'),
        (x2019, '2019'),
        (x2020, '2020'),
        (x2021, '2021'),
    ]
    year = models.CharField(
        choices = YEAR_OPTIONS, 
        default = x2021,
        max_length = 100,
        )

## Nation of Origin
    FRANCE = 'France'
    GERMANY = 'Germany'
    ITALY = 'Italy'
    UNITED_ARAB_EMIRATES = 'United Arab Emirates'
    UNITED_KINGDOM = 'United Kingdom'
    NATION_OF_ORIGIN_OPTIONS = [
        (FRANCE, 'France'),
        (GERMANY, 'Germany'),
        (ITALY, 'Italy'),
        (UNITED_ARAB_EMIRATES, 'United Arab Emirates'),
        (UNITED_KINGDOM, 'United Kingdom'),
    ]
    nation_of_orign = models.CharField(
        choices = NATION_OF_ORIGIN_OPTIONS,
        max_length = 100,
    )
    
    horsepower = models.IntegerField(
        blank = True,
        default = 0,
    )
    image = models.ImageField(
        upload_to = 'carImages',
        blank = True,
    )

    description = models.TextField(
        blank = False
    )

    def __str__(self):
        return "{} - {}".format(self.make, self.model)

    def get_absolute_url(self):
        return reverse("CarsDetail)", kwargs=("pk", self.pk))