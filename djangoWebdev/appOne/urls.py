from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This will be the home page of appOne
    path('home/', views.home, name='home'),
    path('home/theme', views.theme, name='theme'),
    
]
