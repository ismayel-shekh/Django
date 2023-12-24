from django.shortcuts import render

# /home/ismayel/softworar dabvelopement project/Django/project_2/project_2/views.py
# /home/ismayel/softworar dabvelopement project/Django/project_2/template/index.html
def index(request):
    return render(request, 'index.html')