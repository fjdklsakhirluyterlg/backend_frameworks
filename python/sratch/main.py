import socket

PORT = 5030
BUFFER_SIZE = 1024
HOST = ''

def handle_request(client_socket):
    request = client_socket.recv(BUFFER_SIZE).decode()

    print(request)

    request_lines = request.split('\r\n')
    path = request_lines[0].split()[1]

    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"