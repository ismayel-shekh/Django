from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class addCarCreateView(CreateView):
    model = models.car
    form_class = forms.carFrom
    template_name  = 'add_car.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.brand = self.request.user
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.car
    form_class = forms.carFrom
    template_name = 'add_car.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class DeleteCarView(DeleteView):
    model = models.car
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

def showdata(request):
    data = models.car.objects.all()
    return render(request, 'home.html', {'data': data})

# class DetailCarView(DetailView):
#     model = models.car
#     pk_url_kwarg = 'id'
#     template_name = 'detals.html'
#     context_object_name = 'car_app'

#     def car_post(self, request, *args, **kwargs):
#         comment_form = forms.CommentForm(data=self.request.POST)
#         post = self.get_object()
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#         return super().get(request, *args, **kwargs)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post =  self.object
#         comments = post.comments.all()
#         comment_form = forms.CommentForm()

#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context

class DetailPostView(DetailView):
    model = models.car
    pk_url_kwarg = 'id'
    template_name = 'detals.html'
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
        context['comments_form'] = comment_form
        return context

@login_required
def Buycar(request, id):
    b_car = models.car.objects.get(pk= id) 
    if b_car.car_quentiry > 0:
        b_car.car_quentiry -= 1
        b_car.save()
        messages.success(request, 'Car purchased Successfully')
    else:
        messages.error(request, 'This car is not abailable in our stock ')
    return render(request, 'detals.html', {'buycar': b_car})