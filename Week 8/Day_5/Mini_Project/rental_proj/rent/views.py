from django.shortcuts import render, redirect
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate
from .forms import CustomerForm, RentalForm, VehicleForm




def mainpage(request):
    context = {}
    return render(request, 'mainpage.html', context)





def rental(request):
    rentals = Rental.objects.all()
    context = {
        'rentals': rentals,
    }
    return render(request, 'rental.html', context)

def customer(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'customer.html', context)

def vehicle(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles,
    }
    return render(request, 'vehicle.html', context)




def rental_id(request, id):
    rental = Rental.objects.get(id=id)
    context = {
        'rental': rental,
    }
    return render(request, 'rental_id.html', context)

def customer_id(request, id):
    customer = Customer.objects.get(id=id)
    context = {
        'customer': customer,
    }
    return render(request, 'customer_id.html', context)

def vehicle_id(request, id):
    vehicle = Vehicle.objects.get(id=id)
    context = {
        "vehicle": vehicle,
    }
    return render(request, 'vehicle_id.html', context)




def rental_add(request):
    if request.method == 'GET':
        form = RentalForm()
        context = {
            'form': form,
        }
        return render(request, 'rental_add.html', context)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental')
        

def customer_add(request):
    if request.method == 'GET':
        form = CustomerForm()
        context = {
            'form': form,
        }
        return render(request, 'customer_add.html', context)
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')


def vehicle_add(request):
    if request.method == 'GET':
        form = VehicleForm()
        context = {
            'form': form,
        }
        return render(request, 'vehicle_add.html', context)
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle')