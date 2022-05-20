from socket import socket
import subprocess
def scan():
    a = subprocess.check_output(['hcitool','scan'])
    if a==[]:
        return "No devices found"
    else:
        return a
scan()
