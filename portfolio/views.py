
from django.shortcuts import render
from accounts.models import Profile


def home(request):
    return render(request, 'portfolio/home.html')


def about(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
    return render(request, 'portfolio/about.html', {'profile': profile})


def projects(request):
    return render(request, 'portfolio/projects.html')


def contact(request):
    return render(request, 'portfolio/contact.html')
