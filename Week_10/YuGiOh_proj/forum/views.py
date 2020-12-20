from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone


class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    fields = ['title','text']
    # deal with the remaining fields


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    fields = ['title','text']
    # make sure you deal with the remaining fields

@method_decorator(login_required, name='get')
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['title','text']
    # deal with remaining fields in views

@method_decorator(login_required, name='get')
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields = ['title','text']
    # deal with remaining fields in views





# bullshit below detected - make sure you take the garbage out
  
@method_decorator(login_required, name='get')
class CreateComment(View):
    def get(self, request):
        form = CommentForm
        context = {
            'form': form,
        }
        return render(request, 'addcomment.html', context)
    
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(**data)
            return redirect('forum')
        else:
            context = {'invalid_entry':True}
            return render(request, 'addcomment.html', context)


class Forum(ListView):
    template_name='templates/forum.html'
    model = Comment
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context