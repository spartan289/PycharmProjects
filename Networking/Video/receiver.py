import socket, numpy, pickle    # Import Modules
from cv2 import cv2
# AF_INET refers to the address of family of ip4v
# SOCK_DGRAM means connection oriented UDP protocol
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)  # Gives UDP protocol to follow
ip="192.168.0.127"    # Server public IP
port=1    # Server Port Number to identify the process that needs to recieve or send packets
s.bind((ip,port))     # Bind the IP:port to connect
print(s)
# In order to iterate over block of code as long as test expression is true
while True:
    x=s.recvfrom(100000000)    # Recieve byte code sent by client using recvfrom
    clientip = x[1][0]         # x[1][0] in this client details stored,x[0][0] Client message Stored
    print(clientip)
    data=x[0]                  # Data sent by client
    data=pickle.loads(data)    # All byte code is converted to Numpy Code
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)  # Decode
    cv2.imshow('my pickle', data) # Show Video/Stream
    if cv2.waitKey(10) == 13:  # Press Enter then window will close
        break
cv2.destroyAllWindows()        # Close all windows