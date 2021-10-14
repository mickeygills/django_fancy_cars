from django.urls import path
from . import views

# This is a connection -> Supposed to match the name of the app.
app_name = 'restaurants'
#from restaurants.views import GetAllRestaurants


urlpatterns = [
    path('all/', views.GetAllRestaurants.as_view(), name='list_view'),
    path('hello/', views.DummyView.as_view(), name='dummy'),
]