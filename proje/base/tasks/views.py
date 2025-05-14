from django.shortcuts import render

# Create your views here.
tasks=['task1', 'task2', 'task3']

def index(request):
    # This is the view function for the index page
    return render(request, 'tasks/index.html', {'tasks': tasks})
def add(request):
   
    return render(request, 'tasks/add.html')