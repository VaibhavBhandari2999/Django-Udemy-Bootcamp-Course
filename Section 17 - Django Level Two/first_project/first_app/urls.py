from django.urls import path
from first_app import views

urlpatterns=[
    path('', views.index, name='index'),        #The function call in views.py
]
