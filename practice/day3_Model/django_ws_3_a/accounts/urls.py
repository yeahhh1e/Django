from django.contrib import admin
from django.urls import path
from todos import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
]