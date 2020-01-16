from django.shortcuts import render
from django.contrib.auth.models import User
from Game.models import Player
from random import random

def Login(request):
    if request.method == 'POST':
        Player.objects.create(   
        name = request.POST['name'], 
        posX = random() * 100,
        posY = random() * 100,
        radius = 0.5,
        color = '#ffffff'
        )
    return render(request, 'Game/Login.html')
