from django.conf.urls import url
from Game.Information import consumer

websocket_urlpatterns = [
    url('play/', consumer.InformationConsumer),
]