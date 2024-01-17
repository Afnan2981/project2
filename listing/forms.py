from django import forms
from .models import Comment  # Assuming you have a Comment model

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Assuming your Comment model has a 'text' field for the comment text
