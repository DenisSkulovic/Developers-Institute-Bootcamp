from django.shortcuts import render, redirect
from .models import Country, Category, Director, Film
from .forms import AddFilmForm, AddDirectorForm
from django.views import generic



class Homepage(generic.ListView):
    model = Film
    template_name = '../templates/homepage.html'
    
    
class AddFilm(generic.View):
    def get(self, request):
        form = AddFilmForm()
        context = {
            'form': form,
        }
        return render(request, '../templates/film/addFilm.html', context)
    
    def post(self, request):
        form = AddFilmForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect('../templates/homepage.html')


class AddDirector(generic.View):
    def get(self, request):
        form = AddDirectorForm()
        context = {
            'form': form,
        }
        return render(request, '../templates/film/addDirector.html', context)
    
    def post(self, request):
        form = AddDirectorForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect('../templates/homepage.html')