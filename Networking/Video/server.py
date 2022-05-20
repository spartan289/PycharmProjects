import pickle
import struct
import threading

from cv2 import cv2
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost',22000))
print(serverSocket)
serverSocket.listen(5)
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE=409600
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

clientconnected,clientaddress = serverSocket.accept()
def receive():

    data = b''
    payloaf_size = struct.calcsize("Q")
    while True:
        while len(data)<payloaf_size:
            message= clientconnected.recv(BUFFER_SIZE)
            data+=message
        packed_msg_size = data[:payloaf_size]
        data = data[payloaf_size:]
        msg_size = struct.unpack("Q",packed_msg_size)[0]
        while len(data)<msg_size:
            message= clientconnected.recv(BUFFER_SIZE)
            data += message
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)

        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # Decode
        cv2.imshow('frame', frame)
        cv2.waitKey(1)
# def broadcast():
#     video = cv2.VideoCapture(0)
#     while True:
#         ret, frame = video.read()
#         data = pickle.dumps(frame)
#         message_size = struct.pack("Q", len(data))
#         clientConnected.sendall(message_size + data)  ### new code

receive_thread = threading.Thread(target=receive)
receive_thread.start()
# broadcast_thread = threading.Thread(target=broadcast)
# broadcast_thread.start()