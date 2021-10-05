from django.urls import path
from . import views
from Cars.views import CarsListView, CarsDetailView, CarsCreateView, CarsUpdateView, CarsDeleteView


urlpatterns = [
    path('api/', views.CarsListAPIView.as_view(), name='cars_list'),
    path('api/<int:id>/', views.CarsRetrieveAPIView.as_view(), name='cars_detail'),
    path('api/create/', views.CarsCreateAPIView.as_view(), name='cars_create'),
    path('api/update/<int:id>/', views.CarsRetrieveUpdateAPIView.as_view(), name='cars_update'),
    path('api/delete/<int:id>/', views.CarsDestroyAPIView.as_view(), name='cars_delete'),
    #### Django URLS ####
    path('', CarsListView.as_view(), name='CarsList'),
    path('cars/<int:pk>/', CarsDetailView.as_view(), name='CarsDetail'),
    path('create/', CarsCreateView.as_view(), name='CreateCars'),
    path('update/<int:pk>/', CarsUpdateView.as_view(), name='UpdateCars'),
    path('delete/<int:pk>/', CarsDeleteView.as_view(), name='DeleteCars'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
