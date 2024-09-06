from django import forms
from car_manager.models import CommentModel, CarModel
from django.forms.widgets import Textarea
from django.utils import timezone

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


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('make', 'model', 'year', 'description')
        exclude = ('owner',)
        widgets = {
            'description': Textarea(
                attrs={
                    'rows': 4,
                    'cols': 38,
                }
            ),
        }


class UpdateCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('make', 'model', 'year', 'description')
        widgets = {
            'description': Textarea(
                attrs={
                    'rows': 4,
                    'cols': 38,
                }
            ),
        }

