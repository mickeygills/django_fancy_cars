from django import forms
from django.http.response import HttpResponse
from .models import Restaurant
from django.core.mail import send_mail

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'address',
            'city',
            'state',
            'rating'
        ]


class EmailForm(forms.Form):
    fullName = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=500)

    def send_email(self):
        fullName = self.cleaned_data.get('fullName')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')
        from_email = 'mike@congressful.com'
        to_email = ['michael.mcgill@live.com']
        contact_message = f'You just received an email from {fullName}, The message is the following: {message}'
        send_mail(
            'New Email from Django Project',
            contact_message,
            from_email,
            to_email,
            fail_silently=False,
        )
        return HttpResponse('Email was sent successfully.')