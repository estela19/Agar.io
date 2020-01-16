from Game.Game.models import Player 
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
    
