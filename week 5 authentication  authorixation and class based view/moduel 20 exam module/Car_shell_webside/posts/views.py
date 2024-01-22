from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
from django.contrib import messages
from Buy_cars.models import car_buying_history

# Add Post using class Based view


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    context_object_name = 'car_app'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
@login_required
def Buycar(request, id):
    car = models.Post.objects.get(pk=id) 

    if car.car_quantity > 0:
        car.car_quantity -= 1
        car.save()
        Buying = car_buying_history(
            Car_name = car.car_name,
            Price = car.car_price,
            author = request.user,
            image = car.image,
            Car_Details = car.car_detail,
        )
        Buying.save()
        messages.success(request, 'Car purchased Successfully')
        
    else:
        messages.error(request, 'This car is not abailable in our stock ')
    return render(request, 'succes.html', {'car_app': car})