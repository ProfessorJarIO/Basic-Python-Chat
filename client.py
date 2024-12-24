# Client.py

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 19000))
    
    msg = input('=>').encode()
    while True:
        try:
            s.sendall(msg)
            data = s.recv(512)
            
            print(data.decode())
            
            if not data:
                break
            
            msg = input('=> ').encode()
        
        except KeyboardInterrupt:
            break
