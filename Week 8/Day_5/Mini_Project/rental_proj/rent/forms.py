from django.forms import ModelForm
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
    
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'