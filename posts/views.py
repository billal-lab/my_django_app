from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Posts


def index(request):
    # return HttpResponse('HELLO FREINDS')
    posts = Posts.objects.all()

    context = {
        'title': 'posts objects',
        'posts' : posts
    }
    return render(request, 'posts/index.html',context)


def show(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'title': 'one post',
        'post': post
    }
    return render(request, 'posts/show.html', context)
