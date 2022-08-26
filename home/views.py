from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'InfoBlog',
    }
    return render(request, 'home/index2.html', context=context)
