from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from logic import *
from deltatime import *
import time
import json

class InformationConsumer(AsyncWebsocketConsumer):
    # when start connection
    async def connect(self):
        await self.accept()

    # when end connection
    async def disconnect(self, close_code):
        pass

    # when recieve json
    async def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json['name']
        mouseX = text_data_json['x']
        mouseY = text_data_json['y']

        dt = GetDeltaTime(time.time())
        ChangePlayerPosition(name, mouseX, mouseY, dt)
        data = MakeJson(name)        

        await self.send(text_data = data)

        