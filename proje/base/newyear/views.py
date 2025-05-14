from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    now = datetime.now()
    if now.month == 1 and now.day == 1:
        # If today is New Year's Day, return a special message
        newyear=True
    else:
        # Otherwise, return a normal message
        newyear=False
    return render(request, 'newyear/index.html', {'newyear': newyear})
    
  
