from django.shortcuts import render , redirect

from categories.models import Category
from posts.models import Post
def home(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(name = category_slug)
        #not clear that part
        data = Post.objects.filter(category  = category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data' : data, 'category' : categories})

