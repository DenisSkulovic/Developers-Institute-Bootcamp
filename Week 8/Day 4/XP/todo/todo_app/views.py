from django.shortcuts import render, redirect
from .models import Todo, Category
from .forms import TodoForm

def todo_view(request):
    todos = Todo.objects.all()
    if request.method == "GET":
        form = TodoForm()
        context = {
            'todos': todos,
            'todo_form': TodoForm}
        return render(request, 'todo_view.html', context)

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('display_todos')




def display_todos(request):
    todos = Todo.objects.all()
    context={'todos':todos}
    return render(request, 'display_todos.html', context)

