from django.forms import ModelForm
from django import forms
from .models import CookieJar, SaveJoke


class CookieTracker(ModelForm):
    class Meta:
        model = CookieJar
        fields = ['Title', 'Accomplishment']


class SaveJokeForm(ModelForm):
    class Meta:  # Define its meta information:
        model = SaveJoke  # Connect this ModelForm the model object defined in mainapp/models.py
        fields = '__all__'  # '__all__' is a dunder shortcut to grab all the fields within the Product model,
        # define in products/models.pyclass:    #inherit information from ModelForm
