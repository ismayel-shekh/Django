from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_Post(request):
    if request.method == 'POST':
        Post_form = forms.PostForm(request.POST)
        if Post_form.is_valid():
            # Post_form.changed_data['author'] = request.user
            Post_form.instance.author = request.user
            Post_form.save()
            return redirect('add_Post')
    else: 
        Post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : Post_form})
@login_required
def edit_Post(request, id):
    post = models.Post.objects.get(pk=id)
    Post_form = forms.PostForm(instance=post) #old code loading ar gono 0
    # print(post.title)
    if request.method == 'POST':
        Post_form = forms.PostForm(request.POST, instance=post)
        if Post_form.is_valid():
            Post_form.instance.author = request.user
            Post_form.save()
            return redirect('homepage')

    return render(request, 'add_post.html', {'form' : Post_form})
@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')