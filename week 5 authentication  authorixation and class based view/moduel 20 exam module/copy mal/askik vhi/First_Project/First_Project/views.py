from django.shortcuts import render,redirect
from third_app.models import All_Car
from second_app.models import Brand
def Home(request, brand_name = None):
    data= All_Car.objects.all()
    
    if brand_name is not None:
        brands = Brand.objects.get(name = brand_name)
        data = All_Car.objects.filter(Brand_Name = brands)
    
    brand = Brand.objects.all()
        
    return render(request, 'home.html', {'data':data, 'brand':brand})

