from django.urls import path
from rest_framework.authtoken import views

from api.views import CarAPIView, CarDetailAPIView, CommentAPIView


app_name = 'api'

urlpatterns = [
    path('token-auth/', views.obtain_auth_token),
    path('cars/<pk>/', CarDetailAPIView.as_view()),
    path('cars/', CarAPIView.as_view()),
    path('cars/<pk>/comments/', CommentAPIView.as_view()),
]