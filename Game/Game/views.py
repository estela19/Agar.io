from django.shortcuts import render
from django.contrib.auth.models import User
from Game.models import Player

def Login(request):
    if request.method == 'POST':
        name = request.POST['name']
#        u = User(username = name)
#        u.save()
    return render(request, 'Game/Login.html')
