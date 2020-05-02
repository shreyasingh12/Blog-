from django.shortcuts import render
from django.http import HttpResponse
from .models import blogapp
# Create your views here.
def blog_list(request):
    blogapps = blogapp.objects.all()
    return render(request,'blogapp/display.html', {'blogapps':blogapps})

def blog_detail(request, slug):
    return HttpResponse("Heyyy")