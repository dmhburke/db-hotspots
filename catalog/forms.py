from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.choices import *

from catalog.models import Profile, AddReview, TestEntryModel

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

class TestEntryForm(ModelForm):
    name = forms.CharField()

    class Meta:
        model = TestEntryModel
        fields = ('name',)
