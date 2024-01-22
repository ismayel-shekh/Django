from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView , UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator #import dacorator

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
 # add post using class based view
@method_decorator(login_required, name='dispatch') # dspatch means not login user can't acctes that side
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_Post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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

@method_decorator(login_required, name='dispatch')
class EditPostview(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

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
        post = self.object # post model er abject ekhane store korlem\
        comments = post.comments.all()
        comment_form=forms.CommentForm()


        context['comments'] = comments
        context['comments_form'] = comment_form
        return context
 

