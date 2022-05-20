from cv2 import cv2

video = cv2.VideoCapture('http://192.168.0.101:8080/video')
while True:
    ret, frame = video.read()
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break