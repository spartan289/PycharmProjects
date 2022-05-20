import struct
from socket import *
import pickle
from cv2 import cv2
import threading
import pyaudio
host = 'localhost'
port = 22000
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

s = socket(AF_INET,SOCK_STREAM)
# p = pyaudio.PyAudio()
# read_list=[s]
# def callback(in_data, frame_count, time_info, status):
#     for s in read_list[1:]:
#         s.send(in_data)
#     return (None, pyaudio.paContinue)
#
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 output=True,
#                 frames_per_buffer=CHUNK,stream_callback=callback)
s.connect((host,port))
print(s)
SEPARATOR = '<SEPARATOR>'
BUFFER_SIZE = 409600
cap = cv2.VideoCapture(0)
def broadcast():

    while True:

        ret, frame=cap.read()
        ret, buffer = cv2.imencode(".jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY),30])
        data = pickle.dumps(buffer)
        message_size = struct.pack("Q",len(data))
        s.sendall(message_size+data)
# def broadcastaudio():
#     while True:
#         micro = [stream.read(CHUNK)]

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

# receive_thread = threading.Thread(target=receive)
# receive_thread.start()
broadcast_thread = threading.Thread(target=broadcast)
broadcast_thread.start()
