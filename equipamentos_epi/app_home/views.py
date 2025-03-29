from django.shortcuts import render

def home(request):
    return render(request, 'app_home/pages/home.html')
