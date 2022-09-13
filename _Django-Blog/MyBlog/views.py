from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.order_by('-id')

    return render(request, 'MyBlog/index.html', {
        'posts': posts
    })


def see_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'MyBlog/see_post.html', {
        'post': post
    })


def see_library(request):
    library_posts = Post.objects.filter(
        category='11'
    )

    return render(request, 'MyBlog/see_library.html', {
        'library_posts': library_posts
    })


def see_language(request):
    language_posts = Post.objects.filter(
        category='12'
    )

    return render(request, 'MyBlog/see_language.html', {
        'language_posts': language_posts
    })


def see_news(request):
    news_posts = Post.objects.filter(
        category='13'
    )

    return render(request, 'MyBlog/see_news.html', {
        'news_posts': news_posts
    })
