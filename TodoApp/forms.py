from django import forms
from .models import *

class TodoForm(forms.ModelForm):
    todo = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Todos...',
            'style': 'border-radius: 4px;',
        }
    ), )

    class Meta:
        model = TodoList
        fields = [
            'todo',
        ]
    
    def clean(self, *args, **kwargs):
        todo = self.cleaned_data.get('todo')
        return super(TodoForm, self).clean(*args, **kwargs)