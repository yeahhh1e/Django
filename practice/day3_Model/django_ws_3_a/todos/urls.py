from django.contrib import admin
from django.urls import path
from todos import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('<str:work>/', views.detail, name='detail'),
]