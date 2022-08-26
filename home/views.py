from django.shortcuts import render
from blog.models import Post
# Create your views here.


def index(request):
    # traigo los últimos posts
    posts = Post.objects.filter(active=True).order_by('-created_at')[:5]
    context = {
        'title': 'InfoBlog',
        'posts': posts,
    }
    return render(request, 'home/index2.html', context=context)
