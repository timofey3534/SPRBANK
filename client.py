import socket
import sys

s = socket.socket()

port = 12345

s.connect(('127.0.0.1', port))

name = sys.argv[1]

s.send(name.encode())

print (s.recv(1024).decode())
s.close()
