from django.shortcuts import render, get_object_or_404
from .models import Post


def get_date(post):
    return post['date']


# Create your views here.
def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'posts': latest_posts,
    })


def get_posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/posts.html', {
        'posts': posts,
    })


def get_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': post,
        'tags': post.tags.all(),
    })
