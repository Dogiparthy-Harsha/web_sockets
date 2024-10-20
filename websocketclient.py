import asyncio
from websockets.sync.client import connect

def hello():
    dropped_count = 0  # Track any dropped messages
    total_requests = 10000
    
    with connect("ws://localhost:8765") as websocket:
        for i in range(1, total_requests + 1):
            try:
                message = f"Request [{i}] Hello world!"
                websocket.send(message)
                response = websocket.recv()  # Receive modified message from server
                print(f"Received: {response}")
            except Exception as e:
                dropped_count += 1
                print(f"Error occurred: {e}")

    print(f"Total dropped messages: {dropped_count}")

hello()
