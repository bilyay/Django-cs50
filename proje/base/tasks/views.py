from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class TaskForm(forms.Form):
    task = forms.CharField(label="New Task", max_length=100)
    # This is the view function for adding a new task   
    


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    
    # This is the view function for the index page
    return render(request, 'tasks/index.html', {'tasks': request.session["tasks"]}) 


def add(request):
    # This is the view function for adding a new task
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session["tasks"]+= [task]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add.html', {'form': form})
        

    return render(request, 'tasks/add.html', {'form': TaskForm()})