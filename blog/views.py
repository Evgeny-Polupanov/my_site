from datetime import date

from django.shortcuts import render

posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpeg',
        'author': 'Evgeniy',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': """There's nothing like the views you get when hiking in the mountains!
        And I wasn't even prepared for what happened whilst I was enjoying the view!""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae commodi consequatur, cumque ea
        eaque, eosexercitationem fuga illo incidunt iste itaque laudantium libero molestiae nesciunt odit pariatur
        quibusdam recusandae temporibus!""",
    },
    {
        'slug': 'post-1',
        'image': 'mountains.jpeg',
        'author': 'Evgeniy',
        'date': date(2021, 7, 22),
        'title': 'Mountain Hiking1',
        'excerpt': """There's nothing like the views you get when hiking in the mountains!
        And I wasn't even prepared for what happened whilst I was enjoying the view!""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae commodi consequatur, cumque ea
        eaque, eosexercitationem fuga illo incidunt iste itaque laudantium libero molestiae nesciunt odit pariatur
        quibusdam recusandae temporibus!""",
    },
    {
        'slug': 'post-2',
        'image': 'woods.jpeg',
        'author': 'Evgeniy',
        'date': date(2021, 7, 23),
        'title': 'Mountain Hiking2',
        'excerpt': """There's nothing like the views you get when hiking in the mountains!
        And I wasn't even prepared for what happened whilst I was enjoying the view!""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae commodi consequatur, cumque ea
        eaque, eosexercitationem fuga illo incidunt iste itaque laudantium libero molestiae nesciunt odit pariatur
        quibusdam recusandae temporibus!""",
    },
    {
        'slug': 'post-3',
        'image': 'coding.jpeg',
        'author': 'Evgeniy',
        'date': date(2021, 7, 24),
        'title': 'Mountain Hiking3',
        'excerpt': """There's nothing like the views you get when hiking in the mountains!
        And I wasn't even prepared for what happened whilst I was enjoying the view!""",
        'content': """Lorem ipsum dolor sit amet, consectetur adipisicing elit. Beatae commodi consequatur, cumque ea
        eaque, eosexercitationem fuga illo incidunt iste itaque laudantium libero molestiae nesciunt odit pariatur
        quibusdam recusandae temporibus!""",
    },
]


def get_date(post):
    return post['date']


# Create your views here.
def index(request):
    sorted_posts = sorted(posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts,
    })


def get_posts(request):
    return render(request, 'blog/posts.html', {
        'posts': posts,
    })


def get_post(request, slug):
    post = next(post for post in posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post,
    })
