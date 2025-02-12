from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # This will be the home page of appOne/home
    path('theme/', views.theme, name='theme'),
    
]
