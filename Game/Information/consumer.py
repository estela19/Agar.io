from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
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
        posX = text_data_json['x']
        posY = text_data_json['y']

        await self.send(text_data = json.dumps({

        }))

        