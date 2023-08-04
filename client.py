import socket
import time

ip = "172.22.144.1"
port = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    port_no = port
    
    if s.connect_ex((ip, port_no)):
        print("Port is ", port_no, "closed")
    else:
        print("port is ", port_no, "open")
        
    s.sendall(b"How are you")    
    data = s.recv(1024)

    while True:
        sendToServer = input("talk to server: ")
        s.send(sendToServer.encode())
        dataFromServer = s.recv(1024)
        time.sleep(0.2)
        print("Server: ", dataFromServer.decode())
        time.sleep(0.2)
print("recieved ", repr(data))
