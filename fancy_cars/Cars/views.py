from django.db.models.query import prefetch_related_objects
from django.shortcuts import render
from rest_framework import generics
from .serializers import CarsListSerializer, CarsDetailSerializer
from .models import Cars
from restaurants.models import Restaurant

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

## For static HTML page
# from django.shortcuts import render_to_response

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

class CarsByColor(ListView):
    model = Cars
    template_name = "cars/cars_color.html"

    def get_context_data(self, **kwargs):
        context = super(CarsByColor, self).get_context_data(**kwargs)
        color_we_looking_for = self.kwargs['color'].capitalize()

        cars_color = Cars.objects.filter(color__icontains=color_we_looking_for)


        #cars_color = Cars.objects.filter(color__icontains=color_we_looking_for)
        number_of_cars = len(cars_color)
        context['car_colors_list'] = cars_color
        context['message'] = 'Art says Hi'
        context["number_of_cars"] = number_of_cars
        context['color'] = color_we_looking_for
        print("--->", context)
        return context

class CarsByYear(ListView):
    model = Cars
    template_name = 'cars/cars_year.html'

    def get_context_data(self, **kwargs):
        context = super(CarsByYear, self).get_context_data(**kwargs)
        filtered_year = self.kwargs['year']
        all_restaurants = Restaurant.objects.all()
        print(all_restaurants)
        cars_year = Cars.objects.filter(year=filtered_year)
        number_of_cars = len(cars_year)
        
        context['car_years_list'] = cars_year
        context['number_of_cars'] = number_of_cars
        context['year'] = filtered_year
        context['all_restaurants'] = all_restaurants
        return context


class CarsByMake(ListView):
    model = Cars
    template_name = 'cars/cars_make.html'

    def get_context_data(self, **kwargs):
        context = super(CarsByMake, self).get_context_data(**kwargs)
        filtered_make = self.kwargs['make'].capitalize()
    
        cars_make = Cars.objects.filter(make__icontains=filtered_make)
        #cars_make = Cars.objects.filter(make=filtered_make)
        number_of_cars = len(cars_make)
        
        context['car_make_list'] = cars_make
        context['number_of_cars'] = number_of_cars
        context['make'] = filtered_make
        return context
        

class CarsByNation(ListView):
    model = Cars
    template_name = 'cars/cars_nation.html'

    def get_context_data(self, **kwargs):
        context = super(CarsByNation, self).get_context_data(**kwargs)
        filtered_nation = self.kwargs['nation'].capitalize()

        cars_nation = Cars.objects.filter(nation_of_orign__icontains=filtered_nation)
        number_of_cars = len(cars_nation)

        context['car_nation_list'] = cars_nation
        context['number_of_cars'] = number_of_cars
        context['nation'] = filtered_nation
        return context



#objects.filter(entry__headline__contains='Lennon')

## For Static Car Filter HTML File
#def CarsFilter(request):
#   return render_to_response('cars_filter.html')