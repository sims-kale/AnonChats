import asyncio
import websockets
import random

# Storing connected clients
connected = set()

async def chat(websocket, path):
    # Register client
    connected.add(websocket)
    try:
        async for message in websocket:
            print(message)
            # Broadcast message to all connected clients
            for client in connected:
                
                if client != websocket:
                    await client.send(message)
                    


    finally:
        # Remove client when they disconnect
        connected.remove(websocket)

# start_server = websockets.serve(chat, "localhost", 8765)

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
