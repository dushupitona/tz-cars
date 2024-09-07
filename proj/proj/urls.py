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
