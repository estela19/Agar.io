from django.shortcuts import render
from django.contrib.auth.models import User
from Game.models import Player
import random

def Login(request):
    if request.method == 'POST':
        name = request.POST['name']
        X = random.randint(0,100)
        Y = random.randint(0,100)
        Player.objects.create(
            name = name,
            posX = X,
            posY = Y,
            radius = 0.5,
            color = '#ffffff'
        )

    return render(request, 'Game/Login.html')
