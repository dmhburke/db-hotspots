from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.choices import *
import json, requests
from django.contrib.gis.geoip2 import GeoIP2

from catalog.models import Profile, AddReview, MasterAddModel, TestEntryModel

class ProfileForm(UserCreationForm):
    userpic = forms.FileField(required=False)
    location = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'userpic', 'location',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class AddReviewForm(ModelForm):
    user = forms.CharField(required=False)
    name = forms.CharField()
    location = forms.ChoiceField(choices=LOCATION, required=True)
    category = forms.ChoiceField(choices=CATEGORY, required=True)
    spotpic = forms.FileField(required=False)
    perfect_for = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'onclick': 'myFunction();'}),choices=PERFECT_FOR, label='', required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":30}), required=False)
    rating = forms.DecimalField(max_digits=3,decimal_places=1,required=False)

    class Meta:
        model = AddReview
        fields = ('name', 'location', 'category', 'spotpic', 'perfect_for', 'notes', 'rating',)


#TESTPAGE@catalog/testpage

class TestEntryForm(forms.Form):
    city = forms.ChoiceField(choices=CITIES, required=True)
    name = forms.CharField()

    def search(self, request):
    #Ability to get user current IP (doesn't seem very accurate)
        # def get_client_ip(request):
        #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        #     if x_forwarded_for:
        #         ip = x_forwarded_for.split(',')[0]
        #     else:
        #         ip = request.META.get('REMOTE_ADDR')
        #     return ip
        # currentIP = '158.222.246.25' #currentIP = get_client_ip(request)
        # geo = GeoIP2()
        # #IP based location details - CITY
        # # currentLocationDetails = geo.city(currentIP)
        # # currentCity = currentLocationDetails['city']
        # # currentState = currentLocationDetails['region']
        # # currentLocation = str(currentState) + ', ' + str(currentState)
        # #IP-based location detail - LAT/LONG
        # #homeLatLong = '40.734580, -74.003860'
        # # userIPTuple = geo.lat_lon(currentIP)
        # # userLat = userIPTuple[0]
        # # userLong = userIPTuple[1]
        # # userLatLong = str(userLat) + ", " + str(userLong)

        completeQuery = self.cleaned_data['name']
        selectedLocation = self.cleaned_data['city']

        formURL = 'https://api.foursquare.com/v2/venues/suggestcompletion'
        formParams = dict(
            client_id='0PR1PTLMSLBM0ORYW5U2YGL43IOZXFVKWFIC2DHHXOP30Z35',
            client_secret='SJDG5K1D5NARSRZYAAYPJMTJBPIGW4ONUTQBT4HTDNUGSLQQ',
            v='20180323',
            near= selectedLocation, #currentLocation
            query=completeQuery,
            limit=10,
        )

        formResponse = requests.get(url=formURL, params=formParams)
        formStatus = formResponse.status_code
        formDetails = formResponse.content
        formData = formResponse.json()

        return formData

        def get_apiresult_url(self):
             """Returns the url to access a particular instance of the search result"""
             return reverse('testpagedetail', args=[str(self.name)])

class MasterAddForm(ModelForm):
    rating = forms.DecimalField(max_digits=10,decimal_places=8,required=False)
    perfect_for = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'onclick': 'myFunction();'}),choices=PERFECT_FOR, label='', required=False)
    notes = forms.CharField(widget=forms.Textarea(attrs={"rows":2, "cols":30}), required=False)

    class Meta:
        model = MasterAddModel
        fields = ('rating', 'perfect_for', 'notes',)
