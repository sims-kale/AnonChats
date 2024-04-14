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
    print('new client connected')
    # Assign a unique id to new websocket connection
    for client in connected:
                if client == websocket:
                    username = getUsername(userAndWsClientDict)
                    userAndWsClientDict.append({websocket:username})
                    await client.send(username)
                    print(userAndWsClientDict)

    try:
        async for message in websocket:
            print(message)
            # Broadcast message to all connected clients
            for client in connected:
                
                if client != websocket:
                    await client.send(message)
                    
    except websockets.exceptions.ConnectionClosedError as cce:
        print('Connection closed')

    finally:
        # Remove client when they disconnect
        connected.remove(websocket)
        for userAndWsClient in userAndWsClientDict:
            for key, value in userAndWsClient.items():
                if key == websocket:
                    userAndWsClientDict.remove(userAndWsClient)
                    print('Client ' + value + ' removed')
                

# start_server = websockets.serve(chat, "localhost", 8765)

async def main():
    async with websockets.serve(chat, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())

# object by value and object by reference

