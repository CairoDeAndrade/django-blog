from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-id')
    return render(request, 'MyBlog/index.html', {
        'posts': posts
    })
