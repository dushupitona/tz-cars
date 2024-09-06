from django import forms
from car_manager.models import CommentModel
from django.forms.widgets import Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('content',)
        exclude = ('car', 'author')
        widgets = {
            'content': Textarea(
                attrs={
                    'rows': 4,
                    'cols': 40,
                    'placeholder': 'Write your comment.'
                }
            ),
        }