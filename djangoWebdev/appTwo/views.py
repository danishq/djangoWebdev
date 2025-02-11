from django.shortcuts import render

# Create your views here.
def indexTwo(request):
    return render(request, 'appTwo/indexTwo.html')

