import asyncio
import tornado.websocket

class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.connection = None

    async def connect(self):
        while True:
            try:
                print("Connecting to server...")
                self.connection = await tornado.websocket.websocket_connect(self.url)
                print("Connected to server!")
                await self.read_message()
            except Exception as e:
                print(f"Connection failed: {e}")
                await asyncio.sleep(3)

    async def read_message(self):
        while True:
            try:
                message = await self.connection.read_message()
                if message is None:
                    print("Disconnected from server. Reconnecting...")
                    await self.connect()
                else:
                    print(f"Received message: {message}")
            except Exception as e:
                print(f"Error reading message: {e}")
                await asyncio.sleep(3)
                await self.connect()

async def main():
    client = WebSocketClient("ws://localhost:8888/websocket")
    await client.connect()

if __name__ == "__main__":
    asyncio.run(main())
