from django.shortcuts import render
from car.models import car
from brand.models import Category
def showdata(request, Brand = None):
    data = car.objects.all()
    if Brand is not None:
        brands = Category.objects.get(name = Brand)
        data = car.objects.filter(brand_name = brands)
    brand = Category.objects.all()
    return render(request, 'home.html', {'data': data, 'brand': brand})

# def brandwice_car(request, category_slug = None):
#     # data = car.objects.all()
#     if category_slug is not None:
#         category= Category.objects.get(slug = category_slug)
#         # data = car.objects.filter(category=category)
#     category = Category.objects.all()
#     return render(request, 'home.html', {'category': category})