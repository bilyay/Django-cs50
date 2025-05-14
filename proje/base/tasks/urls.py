from django.urls import path
from . import views
app_name = 'tasks'
urlpatterns = [
    # Define your URL patterns here
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
]