from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView


from car_manager.models import CarModel
from car_manager.froms import CommentForm

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login

# <------------ Cars ------------>

class CarListView(ListView):
    model = CarModel
    template_name = 'car_manager/index.html'
    context_object_name = 'car_list'

class CarDetailView(DetailView):
    model = CarModel
    template_name = 'car_manager/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        form.instance.car = self.get_object()
        form.instance.author = request.user

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('car_detail', args=[self.get_object().id]))
    

class UserCarListView(ListView):
    model = CarModel
    template_name = 'car_manager/user_cars.html'
    context_object_name = 'user_car_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset
        
    

# <------------ User ------------>

class CustomLoginView(LoginView):
    template_name = 'car_manager/login.html'
    next_page = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class RegView(FormView):
    form_class = UserCreationForm
    template_name = 'car_manager/reg.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return super().form_valid(form)