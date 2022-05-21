from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {'name': 'Your name', 'email': 'Your email', 'text': 'Your comment'}
