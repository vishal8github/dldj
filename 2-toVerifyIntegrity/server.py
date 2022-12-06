import socket
import hashlib

a=input("Enter the message:")
sha256hex=hashlib.sha256(a.encode()).hexdigest()

s=socket.socket()
print("\nSocket successfully created")

port=9999
s.bind(('localhost',port))
print("\nSocket binded to %s"%(port))

s.listen(1)
print("\nSocket is listening......\n")

while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.send(a.encode())
    c.send(sha256hex.encode())
    print("Message has been sent")
    c.close()
    break
