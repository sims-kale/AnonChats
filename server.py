import asyncio
import websockets
import random
import string
from nameshelper import getUsername

# Store connected clients
connected = set()
names= set()
userAndWsClientDict = []


async def chat(websocket, path):
    # Register client
    connected.add(websocket)
    username = getUsername(userAndWsClientDict)
    print(username + ' joined')
    userAndWsClientDict.append({websocket:username})
    await websocket.send(username)
    
    # Notify other users that new user has joined
    for client in connected: 
                if client != websocket:
                    await client.send(username+' joined')

    try:
        async for message in websocket:
            print(message)
            # Broadcast message to all connected clients
            for client in connected:
                if client != websocket:
                    await client.send(username+'!'+message)
                    
    except websockets.exceptions.ConnectionClosedError as cce:
        print('Connection closed')

    finally:
        # Remove client when they disconnect
        connected.remove(websocket)
        for userAndWsClient in userAndWsClientDict:
            for key, value in userAndWsClient.items():
                if key == websocket:
                    userAndWsClientDict.remove(userAndWsClient)
                    print(value + ' left')
                    # Notify other users that new user has joined
                    for client in connected: 
                        if client != websocket:
                            await client.send(username+' left')

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
    