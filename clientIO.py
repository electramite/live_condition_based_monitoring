import socketio
import random

sio = socketio.Client()

def send_sensor_readings():
    while True:
        x = random.randint(0, 189)
        
        #x = input(f"type your message here {y}")
        sio.emit("my_message", f"{str(x)} °C")
        print(f"{str(x)} °C")
        sio.sleep(1)

@sio.event
def connect():
    print('connection established')

    sio.start_background_task(send_sensor_readings)

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.43.249:4589')
sio.wait()