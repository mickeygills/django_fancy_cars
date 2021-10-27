from django.contrib import admin
from .models import Restaurant, Review, Tag

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Tag)