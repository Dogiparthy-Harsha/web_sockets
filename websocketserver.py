import asyncio
import random
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        random_number = random.randint(1000, 9999)
        modified_message = f"{message} [Random Number: {random_number}]"
        await websocket.send(modified_message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # Keep server running

if __name__ == "__main__":
    asyncio.run(main())
