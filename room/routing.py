from django.urls import path
from . import client

websocket_urlpatterns = [
    path('ws/<str:room_name>/', client.ChatClient.as_asgi()),
]