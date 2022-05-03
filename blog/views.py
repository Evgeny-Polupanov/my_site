from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {
        'message': 'This is the blog',
    })


def get_posts(request):
    return render(request, 'blog/posts.html', {
        'message': 'The list of posts',
    })


def get_post(request, slug):
    return render(request, 'blog/post.html', {
        'message': f'This is {slug} post',
    })
