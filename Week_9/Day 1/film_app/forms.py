from django.forms import ModelForm
from django import forms
from .models import Country, Category, Director, Film


class AddFilmForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class AddDirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'