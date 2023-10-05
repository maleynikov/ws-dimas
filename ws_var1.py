# https://websocket-client.readthedocs.io/en/latest/examples.html#readme-examples

import websocket as ws


URL = "ws://echo.websocket.events"
TIMEOUT = 10

ws.enableTrace(True)

def hello():
    conn = ws.create_connection(URL, timeout=TIMEOUT)
    conn.recv()

    print("sending test message")
    conn.send("Hello Dimas!")

    print("receiving message from server")
    print("result is %s" % conn.recv())

    print("closing connection")
    conn.close()
