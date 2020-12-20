from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)    
    
class Film(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)
    