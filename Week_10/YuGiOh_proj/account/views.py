from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from mainpage.models import (
    Type, Race, Archetype, Cardset, 
    Image, CardPrice, Attribute, Card,
    )
from .forms import ChangePasswordForm, UserSignupForm, ChangePictureForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='get')
class Account(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        context = {'profile':profile}
        return render(request, 'account.html', context)



def viewcards(request):
    profile = Profile.objects.get(user=request.user) ####### insert the user id somehow
    cards = profile.cards
    context = {
        'cards': cards,
    }
    return render(request, 'globaltemplates/viewcards.html', context)
    
    
    
def viewcard(request, id):
    card = Card.objects.filter(id=id)[0]
    context = {'card': card}
    return render(request, 'globaltemplates/viewcard.html', context)
    
    

class Register(View):
    def get(self, request):
        form = UserSignupForm
        return render(request, 'register.html', {'form':form})
    
    def post(self, request):
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('mainpage')
        
        if not form.is_valid():
            form_invalid = True
            return render(request, 'register.html', {'form_invalid':form_invalid})
            
            
class Login(View):
    def get(self, request):
        
        return render(request, 'login.html', {})
        
    def post(self, request):
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            # add invalid login message later
            return redirect('login')


@login_required
def logout(request):
    return redirect('mainpage')


@login_required
def view_account(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'account.html', context)


@method_decorator(login_required, name='get')
class ChangePicture(View):
    def get(self, request):
        form = ChangePictureForm
        context = {
            'form':form,
        }
        return render(request, 'changepicture.html', context)
        
    def post(self, request):
        form = ChangePictureForm(request.POST)
        if form.is_valid():
            user = request.user
            clean_url = form.cleaned_data['picture']
            print(clean_url)
            profile = Profile.objects.get(user=user)
            profile.picture = clean_url
            profile.save()
            return redirect('account')
        else:
            return redirect('changepicture')


@method_decorator(login_required, name='get')
class ChangePassword(View):
    def get(self, request):
        form = ChangePasswordForm
        context = {'form':form}
        return render(request, 'changepassword.html', context)
        
    def post(self, request):
        username = request.user.username
        old_password = request.POST['old_password']
        password1 = request.POST['new_password']
        password2 = request.POST['confirm_new_password']
        if password1 == password2:
            print(username)
            print(old_password)
            user = authenticate(request, username=username, password=old_password)
            user.set_password(password1).save()
            redirect('mainpage')
        else:
            redirect('changepassword')