from django.db.models.query import prefetch_related_objects
from django.shortcuts import render
from rest_framework import generics
from .serializers import CarsListSerializer, CarsDetailSerializer
from .models import Cars

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

###### API Views ####################################
class CarsListAPIView(generics.ListAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsListSerializer

class CarsRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Cars.objects.all()
    serializer_class = CarsDetailSerializer

class CarsCreateAPIView(generics.CreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsDetailSerializer

class CarsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Cars.objects.all()
    serializer_class = CarsDetailSerializer

class CarsDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Cars.objects.all()


###### Django Views ######################


class CarsListView(ListView):
    '''Read/Retrieve'''
    model = Cars

class CarsDetailView(DetailView):
    '''Read/Retrieve'''
    model = Cars

class CarsCreateView(CreateView):
    '''Create'''
    model = Cars
    fields = [
        'make', 
        'model', 
        'price', 
        'color', 
        'year', 
        'nation_of_orign',
        'horsepower',
        'image',
        'description',
    ]
    success_url = reverse_lazy('CarsList')

class CarsUpdateView(UpdateView):
    ''' Update '''
    model = Cars
    fields = [
        'make', 
        'model', 
        'price', 
        'color', 
        'year', 
        'nation_of_orign',
        'horsepower',
        'image',
        'description',
    ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('CarsList')

class CarsDeleteView(DeleteView):
    '''Delete'''
    model = Cars
    success_url = reverse_lazy('CarsList')