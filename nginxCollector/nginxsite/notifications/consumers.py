import json
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from users.models import User
from channels.db import database_sync_to_async

@database_sync_to_async
def get_user(app_key):
    try:
        user = User.objects.get(app_key=str(app_key))
        return user
    except User.DoesNotExist:
        return None 

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        user = await get_user(self.scope["query_string"].decode("utf8").split("=")[1])
        if user:
            self.room_name = 'notification'
            self.room_group_name = self.room_name + '_' + user.username
        
        else:
            self.room_name = 'notification'
            self.room_group_name = self.room_name + '_' + 'anonymous'

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notification_message',
                'message': message
            }
        )

    # Receive message from room group
    async def notification_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
    
    # @sync_to_async
    # def save_message(self, username, room, message):
    #     Message.objects.create(username=username, room=room, content=message)

    