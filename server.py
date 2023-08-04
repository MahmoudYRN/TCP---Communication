import socket
import time

ip = "172.22.144.1"
port = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print("This server is connected to: ", addr)
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

            while True:
                dataFromClient = conn.recv(1024)
                print("Client: ", dataFromClient.decode())
                time.sleep(0.2)
                reply = input("reply: ")
                conn.send(reply.encode())
                time.sleep(0.2)