from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=254)
    
    def __repr__(self):
        return f'{self.name} - {self.phone_number}'
