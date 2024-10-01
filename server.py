import asyncio
import websockets
import json

from db.airtable_helper import getProfileUrl
from util import msg_types, nameshelper

# Store connected clients
connected = set()
names = set()
userAndWsClientDict = []


async def chat(websocket, path):
    # Register client
    connected.add(websocket)

    username = nameshelper.getUsername(websocket)

    # Get profile image by username if no image found get the default image as profile image
    profile_image_url = getProfileUrl(username)
    profile_image_url = getProfileUrl("DEFAULT") if (profile_image_url is None) else profile_image_url

    userAndWsClientDict.append({websocket: username})
    user_details_msg = {
        "msg": {
            "username": username,
            "profile_image_url": profile_image_url
        },
        "msg_type": msg_types.USER_DETAILS,
        "from": "SYSTEM",
    }
    await websocket.send(json.dumps(user_details_msg))
    print(f"{username} joined", flush=True)

    # Notify other users that new user has joined
    try:
        for client in connected:
            if client != websocket:
                user_event_msg = {
                    "msg": username + " joined",
                    "msg_type": msg_types.USER_EVENT,
                    "from": "SYSTEM",
                }
                await client.send(json.dumps(user_event_msg))
    except Exception as e:
        print(f"Connection Closed for {username}\n\n {str(e)}")

    try:
        async for message in websocket:
            # Broadcast message to all connected clients
            for client in connected:
                if client != websocket:
                    chat_msg = {
                        "msg": message,
                        "msg_type": msg_types.CHAT,
                        "from": username,
                    }
                    await client.send(json.dumps(chat_msg))

    except websockets.exceptions.ConnectionClosedError as cce:
        print(f"{username}'s Connection closed", flush=True)

    finally:
        # Remove client when they disconnect
        connected.remove(websocket)
        for userAndWsClient in userAndWsClientDict:
            for key, value in userAndWsClient.items():
                if key == websocket:
                    userAndWsClientDict.remove(userAndWsClient)
                    print(value + " left", flush=True)
                    # Notify other users that new user has joined
                    for client in connected:
                        if client != websocket:
                            user_event_msg = {
                                "msg": username + " left",
                                "msg_type": msg_types.USER_EVENT,
                                "from": "SYSTEM",
                            }
                            try:
                                await client.send(json.dumps(user_event_msg))
                            except Exception as e:
                                print(f"Connection Closed for {username}\n\n {str(e)}")


async def main():
    async with websockets.serve(chat, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
