from django.urls import path
from chat.consumers import MessageConsumer

# Define your WebSocket URL routing here using path
websocket_urlpatterns = [
    path('ws/messages/', MessageConsumer.as_asgi()),  # WebSocket route
]
