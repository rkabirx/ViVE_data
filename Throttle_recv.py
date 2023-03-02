# Receives instruction from ECM regarding Cruise

import socket

TCP_IP = "0.0.0.0"
TCP_PORT = 6653
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print("Connected by ", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    datalist = list(data)
    conn.send(data)  # echo
conn.close()

if datalist[0] > 1:
    print("Increase speed")
elif datalist[0] < 1:
    print("Decrease speed")
else:
    print("Maintain speed")
