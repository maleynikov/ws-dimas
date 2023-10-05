# https://websockets.readthedocs.io/en/stable/index.html

from websockets.sync.client import connect


URL = "wss://ws.postman-echo.com/raw"

def hello():
    with connect(URL) as websocket:
        websocket.send("Hello Dimas!")
        message = websocket.recv()
        print(f"Received: {message}")
