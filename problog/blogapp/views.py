from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts=[
    {
        'author':'shreya singh',
        'title': 'at',
        'content':'frnd',
        'date_posted': 'aj ki',
    },
{
        'author':'shreya singh',
        'title': 'at',
        'content':'frnd',
        'date_posted': 'aj ki',
    },
{
        'author':'shreya singh',
        'title': 'at',
        'content':'frnd',
        'date_posted': 'aj ki',
    },
]
def home1(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,'blogapp/home1.html', context)

def about(request):
    return render(request, 'blogapp/about.html', {'title':'About'})