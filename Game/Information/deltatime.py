import time

time = 0

def GetDeltaTime(timenow) :
    global time
    deltatime = timenow-time
    time = timenow
    
    return deltatime