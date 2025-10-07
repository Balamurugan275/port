from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
from django.shortcuts import render
from accounts.models import Profile

def about(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'about.html', {'profile': profile})
