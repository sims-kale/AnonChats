import asyncio
import websockets
import json
from util import msg_types, nameshelper

# Store connected clients
connected = set()
names = set()
userAndWsClientDict = []


async def chat(websocket, path):
    # Register client
    connected.add(websocket)
    username = nameshelper.getUsername(userAndWsClientDict)
    print(username + ' joined')
    userAndWsClientDict.append({websocket: username})
    await websocket.send(username)

    # Notify other users that new user has joined
    for client in connected:
        if client != websocket:
            user_event_msg = {
                "msg": username + ' joined',
                "msg_type": msg_types.USER_EVENT,
                "from": "SYSTEM"
            }
            await client.send(json.dumps(user_event_msg))

    try:
        async for message in websocket:
            print(message)
            # Broadcast message to all connected clients
            for client in connected:
                if client != websocket:
                    chat_msg = {
                        "msg": message,
                        "msg_type": msg_types.CHAT,
                        "from": username
                    }
                    await client.send(json.dumps(chat_msg))

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
                            user_event_msg = {
                                "msg": username + ' left',
                                "msg_type": msg_types.USER_EVENT,
                                "from": "SYSTEM"
                            }
                            await client.send(json.dumps(user_event_msg))


async def main():
    async with websockets.serve(chat, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
