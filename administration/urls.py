from django.urls import path
from . import views

urlpatterns = [
    path('governing_body/',views.governing_body,name='governing_body'),
    path('teachers/',views.teachers,name='teachers'),
    path('staff/',views.staff,name='staff'),
]

