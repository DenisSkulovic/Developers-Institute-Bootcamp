from django import forms
from .models import Comment

# not sure this is even needed with CreateView - so make sure you are sure
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title','text']