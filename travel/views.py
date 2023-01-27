from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    name = 'About us'

    return render(request, 'about.html', {'name': name})