import socket
import sys


HOST, PORT = "localhost", 9998

data = bytearray([0x33,0x66,0xFF])

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data)

    # Receive data from the server and shut down
    received = sock.recv(1024)

print("Sent:     {}".format(data))
print("Received: {}".format(received))
