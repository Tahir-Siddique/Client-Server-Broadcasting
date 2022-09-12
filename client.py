#!/usr/bin/env python

import pyaudio
import socket
import sys


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096

s = socket.socket()

IP = sys.argv[1] if(len(sys.argv)>1) else '192.168.0.101'
PORT = sys.argv[1] if(len(sys.argv)>1) else 5000
PORT = int(PORT)
s.connect((IP, PORT))
audio = pyaudio.PyAudio()

device_info = audio.get_default_host_api_info()


stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, output=True, frames_per_buffer=CHUNK, output_device_index=device_info['defaultOutputDevice'])

try:
    while True:
        try:
            data = s.recv(CHUNK)
            # print(type(data))
            stream.write(data)
        except:
            print('Error')

except KeyboardInterrupt:
    pass

print('Shutting down')
s.close()
stream.close()
audio.terminate()
