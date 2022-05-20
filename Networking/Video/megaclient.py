import pyaudio
import pickle
import socket
# import sys
# import threading
# import time
import struct
from cv2 import cv2
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('3.142.81.166', 13050))

def audio_broadcast():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print('* recording')
    frames = []
    while True:
        data = [stream.read(CHUNK)]
        data = pickle.dumps(data)

        message_size = struct.pack("Q", len(data))
        s.sendall(message_size + data)

def audio_receive():
    play = pyaudio.PyAudio()
    stream_play = play.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            frames_per_buffer=CHUNK,
                            output=True)
    while True:
        data = b''
        payloaf_size = struct.calcsize("Q")
        while True:
            while len(data) < payloaf_size:
                message = clientconnected.recv(BUFFER_SIZE)
                data += message
            packed_msg_size = data[:payloaf_size]
            data = data[payloaf_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]
            while len(data) < msg_size:
                message = clientconnected.recv(BUFFER_SIZE)
                data += message
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            print(frame)
            stream_play.write(frame[0], CHUNK)

BUFFER_SIZE=2**15

SEPARATOR = '<SEPARATOR>'

def video_broadcast():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame=cap.read()
        ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY),30])
        data = pickle.dumps(buffer)
        message_size = struct.pack("Q",len(data))
        s.sendall(message_size+data)
def receive():
    data = b''
    payloaf_size = struct.calcsize("Q")
    while True:
        while len(data)<payloaf_size:
            data+=s.recv(BUFFER_SIZE)
        packed_msg_size = data[:payloaf_size]
        data = data[payloaf_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        while len(data)<msg_size:
            data+=s.recv(BUFFER_SIZE)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # Decode
        print(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(10)==13:
            break