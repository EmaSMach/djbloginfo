from django.shortcuts import render
from accounts.models import User

# Create your views here.


def index(request):
    users = User.objects.all().values('login_number')
    logins = 0
    for user in users:
        logins += user['login_number']
    context = {
        'login_number': logins
    }
    return render(request, 'home/index.html', context=context)
