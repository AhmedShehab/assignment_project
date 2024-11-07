# Testing why django sockets are not working
import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        await websocket.send(f"Received: {message}")

start_server = websockets.serve(handle_connection, "localhost", 8000)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()