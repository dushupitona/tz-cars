from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


from car_manager.models import CarModel
from car_manager.froms import CommentForm


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
