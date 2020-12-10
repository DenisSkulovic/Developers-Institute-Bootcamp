from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    def __repr__(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class VehicleType(models.Model):
    name = models.CharField(max_length=255)
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name = models.CharField(max_length=255)
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.FloatField()
    size = models.ForeignKey(VehicleSize, null=True, on_delete=models.SET_NULL)
    def __repr__(self):
        return f'{self.real_cost} - {self.size}'
    def __str__(self):
        return f'{self.real_cost} - {self.size}'


class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, null=True, on_delete=models.SET_NULL)
    def __repr__(self):
        return f'{self.rental_date} - {self.return_date}'
    def __str__(self):
        return f'{self.rental_date} - {self.return_date}'


class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    def __repr__(self):
        return f'{self.daily_rate}'
    def __str__(self):
        return f'{self.daily_rate}'


