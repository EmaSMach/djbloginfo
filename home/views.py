from django.shortcuts import render

# from accounts.models import User
# from accounts.models import Statistics


from blog.models import Post
# Create your views here.

def index(request):
    # users = User.objects.all().values('login_number')
    # logins = 0
    # for user in users:
    #     logins += user['login_number']
    # context = {
    #     'login_number': logins
    # }
    # statistic = Statistics.objects.get(id=1)
    # context.update({
    #     'statistic': statistic,
    #     })
    # return render(request, 'home/index.html', context=context)

    # traigo los últimos posts
    posts = Post.objects.filter(active=True).order_by('-created_at')[:3]
    context = {
        'title': 'InfoBlog',
        'posts': posts,
    }
    return render(request, 'home/index2.html', context=context)

