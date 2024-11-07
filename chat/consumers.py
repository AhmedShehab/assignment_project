from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import Message
from .utils import sanitize_name, sanitize_message
class MessageConsumer(AsyncWebsocketConsumer):
    # Store active WebSocket connections
    active_connections = []

    async def connect(self):
        """Accept WebSocket connection and add it to the active connections list."""
        self.active_connections.append(self)
        await self.accept()
        print(f"New connection established: {self}")

    async def disconnect(self, close_code):
        """Remove the WebSocket connection from the active connections list."""
        self.active_connections.remove(self)
        print(f"Connection closed: {self}")

    async def receive(self, text_data):
        """Handle incoming messages from the WebSocket clients."""
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']

        message = sanitize_message(message)
        name = sanitize_name(name)

        await self.save_message(name, message)

        await self.broadcast_message(name, message)


    @database_sync_to_async
    def save_message(self, name, message):
        """Save the message to the database."""
        Message.objects.create(sender=name, content=message)

    async def broadcast_message(self, name, message):
        """Broadcast the received message to all connected WebSocket clients."""
        for connection in self.active_connections:
            await connection.send(text_data=json.dumps({
                'message': message,
                'name': name,
            }))
