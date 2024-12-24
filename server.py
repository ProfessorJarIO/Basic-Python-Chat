# Server.py

import socket

HOST = "127.0.0.1"
PORT = 19000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    
    s.listen()
    
    conn, addr = s.accept()
    
    print(f"Connected by {addr}")
    
    while True:
        try:
            data = conn.recv(512)
            
            print(data.decode())
            
            if not data:
                break
                
            msg = input('=> ').encode()
            
            conn.sendall(msg)
        except KeyboardInterrupt:
            break
