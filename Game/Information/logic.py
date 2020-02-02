from Game.Game.models import Player 
from Game.Game.models import Food
from collections import OrderedDict
import math
import json

def AbsoluteToRelative(PosX, PosY, ax, ay) :
    return PosX - ax, PosY - ay


def RelativeToAbsolute(PosX, PosY, rx, ry) : 
    return PosX + rx, PosY + ry 


def GetSpeed(scale) :
    return scale / (scale ** 1.44) * 10

def GetScreen(scale) :
    pass

def RadiusToScale(radius) :
    return radius

def DistanceNormalie(radius, distance) :
    return 1/RadiusToScale(radius) * distance

def Normalize(x, y) :
    mag = math.sqrt(x * x + y * y)
    return x / mag, y / mag

def LineDistance(p1x, p2x):
    return abs(p1x - p2x)

def ChangePlayerPosition(name, MouseRelativeX, MouseRelativeY, dt) :
    """ Relative position of mouse to Absolute position of client """
    player = Player.objects.filter(name=name)
    MouseAbsoluteX, MouseAbsoluteY = RelativeToAbsolute(player.posX, player.posY, MouseRelativeX, MouseRelativeY)
    dx, dy = Normalize(player.posX - MouseAbsoluteX, player.posY - MouseAbsoluteY)
    speed = GetSpeed(player.radius)
    player.posX = player.posX + dx * dt * speed
    player.posY = player.posY + dy * dt * speed
    player.save()
    CheckMerge()

def IsInScreen(name):
    player = Player.objects.filter(name=name)

    enemyList = []
    foodList = []
    for enemy in Player.objects.all():
        distanceX = LineDistance(player.posX, enemy.posX)
        distanceY = LineDistance(player.posY, enemy.posY)
        if(DistanceNormalie(player.radius, distanceX) <= 8 and DistanceNormalie(player.radius, distanceY) <= 4.5):
            enemyList.append(enemy)

    for food in Food.objects.all():
        distanceX = LineDistance(player.posX, food.posX)
        distanceY = LineDistance(player.posY, food.posY)
        if(DistanceNormalie(player.radius, distanceX) <= 8 and DistanceNormalie(player.radius, distanceY) <= 4.5):
            foodList.append(food)

    return enemyList, foodList

def GetDistance(p1x, p1y, p2x, p2y):
    return math.sqrt((p1x-p2x)**2 + (p1y - p2y)**2)


def CheckMerge():
    objList = []
    for player in Player.objects.all():
        objList.append(player)

    for food in Food.objects.all():
        objList.append(food)

    for i in range(len(objList)-1):
        for j in range(i+1, len(objList)):
            centerDist = GetDistance(objList[i].posX, objList[i].posY, objList[j].posX, objList[j].posY)
            radiusDist = abs(objList[i].radius - objList[j].radius)
            if centerDist <= radiusDist:
                idxSrc, idxTar = i, j
                if objList[idxSrc].radius < objList[idxTar].radius:
                    idxSrc, idxTar = idxTar, idxSrc
                if objList[idxSrc].radius * 0.8 > objList[idxTar].radius:
                    if type(objList[idxSrc]) == type(Player):
                        if type(objList[idxTar]) == type(Food):
                            objList[idxTar].delete()
                            objList[idxSrc].radius += 0.2
                            objList[idxSrc].save()

                        else:
                            objList[idxSrc].radius += objList[idxTar].radius
                            objList[idxSrc].save()
                            objList[idxTar].delete()


def MakeJson(name) :
    user = Player.objects.filter(name=name)
    player = OrderedDict()

    if(user):
        player.setdefault('state', 1)

    else :
        player.setdefault('state', 0)

    player.setdefault('player', user)

    enemy = OrderedDict()
    food = OrderedDict()
    enemylist, foodlist = IsInScreen(name)
    for i in enemylist :
        enemy.setdefault(i.pop['name'], i)

    for i in foodlist :
        idx = 1
        food.setdefault(idx, i)
        idx += 1

    data = OrderedDict()
    data['scope'] = RadiusToScale(user.radius)
    data['player'] = player
    data['enemy'] = enemy
    data['food'] = food

    return json.dumps(data, ensure_ascii=False, indent="\t")