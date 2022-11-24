from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data={
        'title':'Home Page',
        'Message':'This string is passed through view.py'

    }
    return render(request,'abcd/home.html',data)
