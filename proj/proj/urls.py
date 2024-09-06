"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from car_manager.views import CarListView, CarDetailView, CustomLoginView, CustomLogoutView, RegView, \
    UserCarListView, CreateCarView, UpdateCarView, DeleteCarView
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('', CarListView.as_view(), name='index'),
    path('car/<pk>', CarDetailView.as_view(), name='car_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registration/', RegView.as_view(), name='reg'),
    path('mycars/', UserCarListView.as_view(), name='user_cars'),
    path('mycars/create_car/', CreateCarView.as_view(), name='create_car'),
    path('mycars/update_car/<pk>', UpdateCarView.as_view(), name='update_car'),
    path('mycars/<pk>/delete/', DeleteCarView.as_view(), name='delete_car'),
]
