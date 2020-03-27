from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author': 'shubhindia',
        'title' : 'Blog Post 1',
        'content' : 'Blog content 1',
        'date' : 'March 25, 2020'

    },
    {
        'author': 'shubhindia',
        'title' : 'Blog Post 2',
        'content' : 'Blog content 2',
        'date' : 'March 26, 2020'

    }
]
def Home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/about.html', {'title': 'About'})