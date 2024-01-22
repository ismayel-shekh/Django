from typing import Any
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from . import forms
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import DetailView


class DetailPostview(DetailView):
    model = models.All_Car
    pk_url_kwarg = 'id'
    template_name = 'detials_page.html'
    context_object_name = 'third_app'
    
    
    def post(self, request, *args, **kwargs):
            comment_form = forms.Car_comment(data=self.request.POST)
            post = self.get_object()
            
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
            return self.get( request, *args, **kwargs)
                
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form =forms.Car_comment()
           
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        

@login_required
def BuyCar(request,id):
    car = models.All_Car.objects.get(pk= id)
        
    if car.Quantity > 0:
        car.Quantity -= 1
        car.save()
        messages.success(request,'Car purchased Successfully')
    else:
        messages.error(request,'This car not abailable in our stock')
        
    return render(request, 'detials_page.html', {'third_app': car})
