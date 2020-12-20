from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone

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