from django.urls import path
from . import views

urlpatterns = [
    path('indexTwo/', views.indexTwo, name='indexTwo')
]
