import socket

PORT = 5030
BUFFER_SIZE = 1024
HOST = ''

def handle_request(client_socket):
    request = client_socket.recv(BUFFER_SIZE).decode()

    print(request)

    request_lines = request.split('\r\n')
    path = request_lines[0].split()[1]