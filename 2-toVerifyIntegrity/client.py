import socket
import hashlib

c=socket.socket()

port=9999
c.connect(('localhost',port))

a=c.recv(1024).decode()
data=c.recv(1024).decode()
print("\nWelcome to the network")
c.close()

hexcode=hashlib.sha256(a.encode()).hexdigest()

if hexcode==data:
    print("Integrity of data is maintained")
    print(f"message:{a}")
else:
    print("Integrity of data is lost")
