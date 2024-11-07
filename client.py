import asyncio
import websockets
import json
# This was a way to send messages through a terminal client but i had a problem showing broadcasted messages
#! This is not used

async def listen_for_messages(websocket):
    """Continuously listen for messages from the WebSocket server."""
    while True:
        try:
            # Receive the response from the WebSocket server
            response = await websocket.recv()
            print("Received message:", response)  # Debugging line
            data = json.loads(response)  # Decode the received JSON data
            print(f"Message from {data['name']}: {data['message']}")
        except websockets.ConnectionClosed:
            print("Connection closed.")
            break

async def send_message(websocket, name):
    """Send messages to the WebSocket server."""
    while True:
        # Ask for user's message input
        message_text = input(f"Enter your message, {name}: ")

        # Prepare the message with the name and custom message
        message = {
            "name": name,
            "message": message_text
        }

        # Send the message to the WebSocket server
        await websocket.send(json.dumps(message))

async def main():
    uri = "ws://localhost:8000/ws/messages/"

    # Connect to the WebSocket server
    async with websockets.connect(uri) as websocket:
        # Ask the user for their name once
        name = input("Enter your name: ")

        # Start listening for incoming messages in the background
        asyncio.create_task(listen_for_messages(websocket))

        # Keep asking for user input to send messages
        await send_message(websocket, name)

# Use asyncio.run() to run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
