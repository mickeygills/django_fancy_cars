from django.urls import path
from . import views

# This is a connection -> Supposed to match the name of the app.
app_name = 'restaurants'
#from restaurants.views import DummyView


urlpatterns = [
    path('all/', views.GetAllRestaurants.as_view(), name='list_view'),
    path('rating/<int:rating>/', views.FilterByRating.as_view(), name='rating_view'),
    path('review/<int:pk>/', views.RestaurantDetailView.as_view(), name='RestaurantDetail'),
    path('newreview/<int:pk>/', views.NewRestaurantDetailView.as_view(), name='NewRestaurantDetail'),
    path('review/tag/<banana>/', views.FilterByTag.as_view(), name='tag_view'),
    path('createrestaurant/', views.RestaurantFormView.as_view(), name='form_restaurant'),
    path('contactus/', views.EmailFormView.as_view(), name='form_email'),
]


