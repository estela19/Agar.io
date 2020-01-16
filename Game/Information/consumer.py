from channels.generic.websocket import WebsocketConsumer
import json

class InformationConsumer(WebsocketConsumer):
    # when start connection
    def connect(self):
        self.accept()

    # when end connection
    def disconnect(self, close_code):
        pass

    # when recieve message
    def recieve(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # resend message to client
        self.send(text_data = json.dumps({
            'message' : message
        }))
