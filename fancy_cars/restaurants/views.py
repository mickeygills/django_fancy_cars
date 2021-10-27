from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Restaurant, Review, Tag
from .forms import RestaurantForm, EmailForm
from django.urls import reverse

from django.views.generic import DetailView

# Create your views here.
## Using (View) because this is not a generic view.
class GetAllRestaurants(View):
    # Get Method is a top level method.
    '''
    This is a top-level method, and there’s one for each HTTP verb - 
    get(), post(), patch(), etc. You would override it when you want 
    to do something before a request is processed by the view, or after. 
    But this is only called when a form view is loaded for the first time, 
    not when the form is submitted. Basic example in the documentation. 
    By default it will just render the configured template and return the HTML.
    '''
    def get(self, request):
        res = Restaurant.objects.all()
        tags = Tag.objects.all()
        return render(request, 'restaurants/all_restaurants.html', {'query_set':res, 'tags':tags, 'message':'hello'})



    '''Read/Retrieve'''
    #model = Restaurant

class FilterByRating(View):
    # Get Method is a top level method.
    def get(self, request, **kwargs):
        # print(dir(request.GET))
        # print(request.GET)
        # print(kwargs)

        res = Restaurant.objects.filter(rating__gte=kwargs['rating'])
        print(res)
        return render(request, 'restaurants/restaurants_rating.html', {'filter_restaurants':res, 'message':'hello'})


class FilterByTag(View):

    def get(self, request, **kwargs):
        print('######################', kwargs)
        res_tag = Restaurant.objects.filter(tag=kwargs['banana'])
        print(res_tag)
        return render(request, 'restaurants/restaurants_tag.html', {'filter_restaurants':res_tag, 'message':'##########'})



class RestaurantDetailView(DetailView):
    '''Read/Retrieve'''
    model = Restaurant

class NewRestaurantDetailView(View):
    def get(self, request, **kwargs):
        print(kwargs)
        restaurant_id = kwargs['pk']
        joint = Restaurant.objects.get(pk=restaurant_id)
        print(joint)

        #reviews = Review.objects.filter(restaurant = joint)
        #print(reviews)
        return render(request, 'restaurants/newrestaurant.html', {'one_restaurant':joint})

class RestaurantFormView(View):
    form_class = RestaurantForm

    def get(self, request):
        print('Comes from Get Method', request.GET)
        form = self.form_class
        return render(request, 'restaurants/formrestaurant.html', {'form':form})

    def post(self, request):
        print('From POST Method', request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('restaurants:list_view'))
        else: 
            return render(request, 'restaurants/formrestaurant.html', {'form':form})


class EmailFormView(View):
    form_class = EmailForm
    template_name = 'restaurants/formemail.html'
    success_url = 'restaurants/all/'
    
    def get(self, request):
        print('Comes from Get Method', request.GET)
        form = self.form_class
        return render(request, self.template_name, {'form':form})


    def form_valid(self, form):
        form.send_email()
        return super(EmailFormView, self).form_valid(form)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.send_email()
            return HttpResponse("Have a good day")