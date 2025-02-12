from django.urls import path
from . import views

urlpatterns = [
    path('appTwo/indexTwo/', views.indexTwo, name='indextwo'),
]
