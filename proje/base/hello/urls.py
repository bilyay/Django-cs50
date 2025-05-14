
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('greet/<str:name>/', views.greet, name='greet_with_name'),
]
