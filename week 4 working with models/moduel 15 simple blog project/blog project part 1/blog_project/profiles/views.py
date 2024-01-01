from django.shortcuts import render, redirect
from . import froms
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile_form = froms.profileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form=froms.profileForm()
    return render(request, 'add_profile.html', {'form' : profile_form})