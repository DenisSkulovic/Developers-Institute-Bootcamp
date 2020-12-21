from django.shortcuts import render, redirect
from forum.models import Comment
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone

class CommentDeleteView(DeleteView):
    model = Comment
    success_url ="comment_list/"

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    fields = ['title','text', 'post_date', 'user']


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    fields = ['title','text', 'post_date', 'user']


@method_decorator(login_required, name='get')
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['title','text']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='get')
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields = ['title','text']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context





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