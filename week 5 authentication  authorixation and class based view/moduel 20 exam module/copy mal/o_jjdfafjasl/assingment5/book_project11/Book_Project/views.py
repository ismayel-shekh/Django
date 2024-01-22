from django.shortcuts import render
from UserSite.models import PostModel, CategoryModel

def Home(request, category_slug = None):
    data = PostModel.objects.all()
    
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = PostModel.objects.filter(category = category)
    category = CategoryModel.objects.all()
    
    return render(request,'home.html', {'data': data, 'category':category})


