from django.shortcuts import render, redirect
from forum.models import Comment, Reply
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




class ReplyCreateView(LoginRequiredMixin, CreateView):
    model = Reply
    fields=['text']
    template_name='reply_create.html'

    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_create.html'
    fields = ['title','text']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url ="comment_list/"
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    fields = ['title','text', 'post_date', 'user']
        


class CommentListView(ListView):
    model = Comment
    template_name = 'comment_list.html'
    fields = ['title','text', 'post_date', 'user']




class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'comment_update.html'
    fields = ['title','text']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context