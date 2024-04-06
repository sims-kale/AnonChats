import websockets
import asyncio
import random

# Creating WebSocket server
async def ws_server(websocket):
    print("WebSocket: Server Started.")

    try:
        while True:
            # Receiving values from client
            name = await websocket.recv()

            # Prompt message when any of the field is missing
            if name == "":
                print("Error Receiving Value from Client.")
                break

            # Printing details received by client
            print("Details Received from Client:")

            # Sending a response back to the client
            response = random.randint(1, 10)
            print(f"Hello {name} your luck number is ", response)
            await websocket.send(str(response))

    except websockets.ConnectionClosedError:
        print("Internal Server Error.")

async def main():
    async with websockets.serve(ws_server, "localhost", 8000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
