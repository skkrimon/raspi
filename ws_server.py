import websockets
import asyncio
import json

PORT = 8765

print(f'Server is listening on port {PORT}')

async def echo(ws, path):
    print('A client just connected')
    try:
        async for message in ws:
            print('Received message from client: ' + message)
            try:
                message_json = json.loads(message)
            except:
                await ws.send('ERROR: invalid json')
            await ws.send('Pong: ' + message)
    except ws.exceptions.ConnectionClosed as e:
        print('A client just disconnected')
        
        
start_server = websockets.serve(echo, 'localhost', PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
