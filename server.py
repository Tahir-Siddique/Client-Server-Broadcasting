#!/usr/bin/env python

import pyaudio
import socket
import select
# from datetime import datetime

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096

audio = pyaudio.PyAudio()
device_info = audio.get_default_host_api_info()
serversocket = socket.socket()



IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
print(f"\n\nIP: {IP}\nPORT: {PORT}\n\n")
serversocket.bind((IP, PORT))
serversocket.listen(5)


def callback(in_data, frame_count, time_info, status):
    for s in read_list[1:]:
        try:
            s.send(in_data)
        except:
            pass
    return (None, pyaudio.paContinue)

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK,input_device_index=device_info['defaultInputDevice'], stream_callback=callback)
read_list = [serversocket]
try:
    while True:
        
        try:
            readable, writable, errored = select.select(read_list, [], [])
            for s in readable:
                if s is serversocket:
                    (clientsocket, address) = serversocket.accept()
                    read_list.append(clientsocket)
                    print("Connection from:", address)
                else:
                        data = s.recv(1024)
                        if not data:
                            read_list.remove(s)
        except ConnectionResetError:
            pass
        except:
            print("Error")
            
except KeyboardInterrupt:
    pass


print("finished recording")

serversocket.close()
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()