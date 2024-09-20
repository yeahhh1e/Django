from django.urls import path
# 명시적 상대 경로
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.greeting),
]