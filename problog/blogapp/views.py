from django.shortcuts import render
from .models import blogapp
# Create your views here.
def display(request):
    blogapps = blogapp.objects.all()
    return render(request,'blogapp/display.html', {'blogapps':blogapps})