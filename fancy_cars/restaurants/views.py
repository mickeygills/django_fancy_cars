from django.shortcuts import render
from django.views import View
from .models import Restaurant

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
        print(res)
        print('Hello')


    '''Read/Retrieve'''
    #model = Restaurant

class DummyView(View):
    def get(self, request):
        print("Hello")