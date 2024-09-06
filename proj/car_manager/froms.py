from django import forms
from car_manager.models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('content',)
        exclude = ('car', 'author')