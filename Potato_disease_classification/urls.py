from django.contrib import admin
from django.urls import path
from Potato_disease_classification import views

urlpatterns = [
    path('Potato-Disease-Classification/',views.potato_disease_classifcation,name='potato_disease_classifcation'),
]