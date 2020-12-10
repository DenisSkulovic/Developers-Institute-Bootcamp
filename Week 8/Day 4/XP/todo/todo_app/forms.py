from django import forms
from .models import Todo, Category, CATEGORY_CHOICES


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        title = forms.MultipleChoiceField(widget = forms.Select(choices=CATEGORY_CHOICES))