from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.order_by('-id')

    return render(request, 'MyBlog/index.html', {
        'posts': posts
    })


def see_post(request, post_id):
    post_page = Post.objects.get(id=post_id)

    return render(request, 'MyBlog/see_post.html', {
        'post_page': post_page
    })
