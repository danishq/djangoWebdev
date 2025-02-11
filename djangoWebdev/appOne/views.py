from django.shortcuts import render

def home(request):
    return render(request, 'appOne/home.html')  # Ensure this matches your template path

def theme(request):
    return render(request, 'appOne/theme.html')