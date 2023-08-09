from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('Marksheet', views.marksheet),
    path('Save_Marks', views.saveinfo)
]
