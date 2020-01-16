from Game.Game.models import Player 
from Game.Game.models import Food
import math

def AbsoluteToRelative(name, ax, ay) :
    player = Player.objects.filter(name=name)
    player.posX += ax
    player.posY += ay
    player.save()


def RelativeToAbsolute(PlayerX, PlayerY, rx, ry) :
    return PlayerX + rx, PlayerY + ry


def GetSpeed(scale) :
    return scale / (scale ** 1.44) * 10


def Normalize(x, y) :
    mag = math.sqrt(x * x + y * y)
    return x / mag, y / mag


def ChangePlayerPosition(PlayerAbsoluteX, PlayerAbsoluteY, MouseRelativeX, MouseRelativeY, dt) :
    """ Relative position of mouse to Absolute position of client """
    MouseAbsoluteX, MouseAbsoluteY = RelativeToAbsolute(PlayerAbsoluteX, PlayerAbsoluteY, MouseRelativeX, MouseRelativeY)
    dx, dy = Normalize(PlayerAbsoluteX - MouseAbsoluteX, PlayerAbsoluteY - MouseAbsoluteY)
    return PlayerAbsoluteX + dx * dt, PlayerAbsoluteY + dy * dt


def GetDistance(p1x, p1y, p2x, p2y):
    return math.sqrt((p1x-p2x)**2 + (p1y - p2y)**2)


def CheckMerge(playerDB:Player, foodDB:Food):
    objList = []
    for player in playerDB.objects.all():
        objList.append(player)

    for food in foodDB.objects.all():
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
                            # TODO: Implement add radius
                        else:
                            # TODO: Implement merge
