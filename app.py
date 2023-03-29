import os
import socket

IP = "0.0.0.0"
PORT = 8080
CONTENT_DIR = "/data"

server = socket.socket()
server.bind((IP, PORT))
server.listen()

HEADER = """HTTP/1.1 200 OK
Content-type: text/html

"""
HTML = f"""<h1 style="color:red">Welcome to Podman Container\
Powered Python Dynamic Web Application</h1>
<br>
<h2>Here is the List of All Files Present in {CONTENT_DIR}</h2>
<br>
"""

while True:
    client, addr = server.accept()
    request = client.recv(1024).decode()
    print(f"{addr[0]}:{addr[1]} - {request}")
    try:
        FILES = os.listdir(CONTENT_DIR)
        FILES = "<br>".join(FILES)
    except Exception as err:
        print(f"<br>Error: {err}")
    RESPONSE = HEADER+HTML+"<br>"+FILES
    client.send(RESPONSE.encode())
    client.close()

server.close()
    


