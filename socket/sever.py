import socket

HOST = 'localhost'
port = 1337

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,port))
s.listen(1)

conn, addr = s.accept()
print(f"connected by {addr}")

while 1 :
    data = conn.recv(1024)
    if not data: break #沒接收到數據





