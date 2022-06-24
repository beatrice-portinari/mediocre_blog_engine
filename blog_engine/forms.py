from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'body')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'field_style'}),
            'body': forms.Textarea(attrs={'class': 'field_style'})
        }