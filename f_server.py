from aiohttp import web
import socketio

sio = socketio.AsyncServer()

app = web.Application()

sio.attach(app)

async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')


@sio.event
async def my_message(sid, data):
    print(data)
    await sio.emit('message', str(data))
@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: ", sid)
    print(message)
    


app.router.add_get('/', index)


if __name__ == '__main__':
    web.run_app(app, port=4589)