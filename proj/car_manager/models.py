from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import User


year_validator = RegexValidator(r'^\d{4}$')

class CarModel(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    year = models.CharField(max_length=4, validators=[year_validator])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} | {self.model} | {self.year}' 


class CommentModel(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(to=CarModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
