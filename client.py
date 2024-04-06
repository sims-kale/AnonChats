import websockets
import asyncio

# The main function that will handle connection and communication
# with the server
async def ws_client():
    print("WebSocket: Client Connected.")
    url = "ws://127.0.0.1:8000"
    # Connect to the server
    async with websockets.connect(url) as ws:
        while True:
            name = input("Your Name (type 'exit' to quit): ")

            if name == 'exit':
                break

            # Send values to the server
            await ws.send(name)

            # Receive and print the response from the server
            response = await ws.recv()
            print("Response from server:", response)

# Start the connection
asyncio.get_event_loop().run_until_complete(ws_client())